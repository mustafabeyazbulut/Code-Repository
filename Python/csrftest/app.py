from flask import Flask, Response, abort, redirect, render_template, request, url_for
from hashlib import sha256,md5
from random import randrange

from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)

######## CSRF Token oluşturma ve kontrol

def random_string(length=24):
    rv = ''
    for i in range(length):
        rv += chr(randrange(256))
    return rv

def get_token(secret, user_hash):
    text = "%s%s" % (secret, user_hash)
    return sha256(text.encode('utf-8')).hexdigest()


def check_token(token, secret, user_hash):
    return token == get_token(secret, user_hash)

secret = random_string(length=32)
#######

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="randomkeyflasktest",
)

login_manager = LoginManager()
login_manager.init_app(app)


# database - user bilgileri ve bakiyesi
users = [
    {
        "id": 1,
        "username": "test",
        "password": "test",
        "balance": 20000,
        "user-hash": "",
    },
    {
        "id": 2,
        "username": "user1",
        "password": "user1",
        "balance": 15000,
        "user-hash": "",
    },
]

# @app.after_request    #  Response da token'ı basar. Hata durumunda kontrol amaçlı ekledim.
# def csrftoken(response):
#     if current_user.is_authenticated:
#         token = get_user(current_user.id)["user-hash"]
#         response.headers['X-CSRF-Token'] = get_token(secret, token)
#         return response
#     else:
#         return response

@app.before_request # İstek çalışmadan önce CSRF token'ının geçerli olup olmadığını kontrol eder ve sonrasında yeni token oluşturur.
def csrf_protect():
    if current_user.is_authenticated and request.method == "POST":
        token = request.form.get("token")
        if not check_token(token, secret, get_user(current_user.id)["user-hash"]):
            abort(406)
        user_hash = sha256(random_string().encode('utf-8')).hexdigest()
        get_user(current_user.id)["user-hash"] = user_hash

class User(UserMixin):
    ...


def get_user(user_id: int):
    for user in users:
        if int(user["id"]) == int(user_id):
            return user
    return None


@login_manager.user_loader
def user_loader(id: int):
    user = get_user(id)
    if user:
        user_model = User()
        user_model.id = user["id"]
        return user_model
    return None


@app.errorhandler(401)
def unauthorized(error):
    return Response("Not authorized"), 401

@app.errorhandler(406)
def csrferror(error):
    return Response("CSRF Token Error"), 406

@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        for user in users:
            if user["username"] == username and user["password"] == password:
                user_model = User()
                user_model.id = user["id"]                
                response = redirect(url_for("accounts"))
                user_hash = md5(random_string().encode('utf-8')).hexdigest()
                user["user-hash"] = user_hash
                login_user(user_model)
                return response
        else:
            return render_template("index.html", error_msg="Hatalı Kullanıcı Adı veya Parola")
        
    if current_user.is_authenticated:
        return redirect(url_for("accounts"))

    return render_template("index.html")


@app.route("/accounts", methods=["GET", "POST"])
@login_required
def accounts():
    user = get_user(current_user.id)
    error_msg = ""
    if request.method == "POST":    # Para transferi
        amount = int(request.form.get("amount"))
        account = int(request.form.get("account"))
        transfer_to = get_user(account)

        if not transfer_to:
            error_msg = "Hatalı Hesap Numarası"
        elif amount > user["balance"]:
            error_msg = "Yetersiz Bakiye"
        elif amount<=0:
            error_msg = "Hatalı Tutar"
        else:
            user["balance"] -= amount
            transfer_to["balance"] += amount
        
        
    resp = render_template("accounts.html", balance=user["balance"], username=user["username"], csrf_token=get_token(secret, user["user-hash"]),error_msg=error_msg)
    return resp

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))

if __name__ == "__main__":
    app.run(debug=True)
