import math
text=["duran duran sang wild boys in 1984",
      "wild boys don't remain forever wild",
      "who brought wild flowers",
      "it was john krakauer who wrote in to the wild"]
toplamCümleSayisi=len(text)
benzersizTerimler=[]
tfidf_liste=[]
def t_terimi_geçen_cümle_sayısı(terim):# her bir terimin kaç cümlede oldugunu gösteren fonksiyon
      a=0
      kaçcümledevar=0
      cumle=[]
      while a <len(text):
            cumle=text[a].split(" ")
            for i in range (len(cumle)):
                  if(terim==cumle[i]):
                        kaçcümledevar=kaçcümledevar+1
                        break
            a=a+1
      return kaçcümledevar

sayaç=0
while sayaç<len(text):# text teki her bir terimi ayırma ve sonra benzersiz olanları bir listeye aktarma yaptım
      tek=text[sayaç]
      for i in tek.split():
            if i not in benzersizTerimler:
                   benzersizTerimler.append(i)
      sayaç=sayaç+1

z=0
tftd=0
while z<len(text):#text teki her cümleye göre ayırdık ve tek tek cümlelrin idft degerini hesaapladık
      cumle=text[z].split(" ")
      x=0
      while x<len(benzersizTerimler):# benzersiz terimlerin tek tek idf degerini ve tfidf degerini hesaplayıp tfidf degerlerini listeye attık.
            terim=benzersizTerimler[x]
            idf=math.log10(toplamCümleSayisi/t_terimi_geçen_cümle_sayısı(terim))#idf degrini hesapladık
            tftd=0
            for i in range (len(cumle)):
                  if(terim==cumle[i]):
                        tftd=tftd+1           
            thidf=tftd*idf
            
            thidf=round(thidf,3)#ondalıklı sayıyı virgülden sonra 3 basamaklı yazma fonksiyonu
            tfidf_liste.append(thidf)
            x=x+1
      z=z+1

print(benzersizTerimler)
print(tfidf_liste[0:19])
print(tfidf_liste[19:38])
print(tfidf_liste[38:57])
print(tfidf_liste[57:76])
