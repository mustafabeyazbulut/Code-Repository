import math

text=["duran duran sang wild boys in 1984","wild boys don't remain forever wild",
      "who brought wild flowers","it was john krakauer who wrote in to the wild"]

def ayircumle(text):
    liste = []
    for i in text:
        cumle = i.split()
        liste.append(cumle)
    return liste

def ayirkelime(text):
    liste = []
    for i in text:
        newtext = i.split()
        for j in newtext:
            if j not in liste:
                liste.append(j)
    return liste


def cumlesayisi(text, kelime):
    sayac = 0
    for i in text:
       if kelime in i.split():
           sayac += 1
    return sayac

def idf(text, kelime):
    N=len(text)
    idf = math.log10(N/cumlesayisi(text, kelime))
    return idf

words = ayirkelime(text)
sentences = ayircumle(text)
print(words)

for i in sentences:
    liste = []
    for j in words:
        tfidf = i.count(j)*idf(text,j)
        liste.append(round(tfidf,3))
    print(liste)