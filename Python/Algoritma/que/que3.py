def replace_head_tail(str1,X,Y):
    if(len(str1)==0):
        return "Kelime giriniz"
    else:
        space=str1.find(" ")
        newstr1=str1[space+Y:len(str1)]+ str1[X:space]+  str1[space:(space+Y)]+str1[0:X]   
    return newstr1

str1=str(input("2 kelime:"))
X=4
Y=3
print (replace_head_tail(str1,X,Y))





