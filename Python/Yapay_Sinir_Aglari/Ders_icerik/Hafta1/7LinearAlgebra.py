"""-------------Lineer Cebir---------------
:etiket:sec_linear-cebir

Artık verileri depolayıp işleyebildiğinize göre, bu kitapta ele alınan modellerin çoğunu anlamak 
ve uygulamak için ihtiyaç duyacağınız temel lineer cebirin alt kümesini kısaca gözden geçirelim. 
Aşağıda, lineer cebirdeki temel matematiksel nesneleri, aritmetiği ve işlemleri tanıtıyoruz, 
bunların her birini matematiksel notasyon ve karşılık gelen kod uygulamasıyla ifade ediyoruz. """

import torch

x = torch.tensor(3.0) # 3.0 sayısını bir tensor haline getirdik
y = torch.tensor(2.0) # 2.0 sayısını bir tensor haline getirdik
print(x)
print(x + y, x * y, x / y, x**y)
#tensor(5.) tensor(6.) tensor(1.5000) tensor(9.)


""" ---------------Vektörler-------------------

[Bir vektörü basitçe skaler değerlerin bir listesi olarak düşünebilirsiniz.] 
Bu değerlere vektörün öğeleri (girişler veya bileşenler) diyoruz. 
Vektörlerimiz veri kümemizden örnekleri temsil ettiğinde, değerleri gerçek dünyada bir miktar önem taşır. 
Örneğin, bir kredinin temerrüde düşme riskini tahmin etmek için bir model eğitiyor olsaydık, 
her başvuru sahibini, bileşenleri gelirlerine, çalışma sürelerine, önceki temerrüt sayılarına 
ve diğer faktörlere karşılık gelen bir vektörle ilişkilendirebilirdik. 
Hastanedeki hastaların potansiyel olarak karşılaşabilecekleri kalp krizi riskini inceliyor olsaydık, 
her hastayı bileşenleri en son yaşamsal belirtilerini, kolesterol düzeylerini, günlük egzersiz dakikalarını vb. 
yakalayan bir vektörle temsil edebilirdik. kalın yüzlü, küçük harfli vektörler (örneğin, x , y ve z) .

Tek boyutlu tensörler aracılığıyla vektörlerle çalışıyoruz. 
Genel olarak tensörler, makinenizin bellek sınırlarına bağlı olarak keyfi uzunluklara sahip olabilir. """

x = torch.arange(4) # 0 dan 3 e kadar 4 sayı üretildi
print('\n',x)
# tensor([0, 1, 2, 3])


""" Bir alt simge kullanarak bir vektörün herhangi bir elemanına atıfta bulunabiliriz. 
Örneğin, x'in i. elemanına xi ile atıfta bulunabiliriz. 
xi öğesinin bir skaler olduğuna dikkat edin, bu nedenle yazı tipine atıfta bulunurken kalın yazı tipini kullanmıyoruz. 
Kapsamlı literatür, sütun vektörlerini vektörlerin varsayılan yönlendirmesi olarak kabul eder, bu kitap da öyle. 
Matematikte, bir x vektörü şu şekilde yazılabilir:
                                                    x = [x1, x2, ..., xn]
:eqlabel:eq_vec_def

burada x1,…,xn vektörün elemanlarıdır. Kodda, (tensöre indeksleyerek herhangi bir öğeye erişiriz.) """
print('\n',x[3])
# tensor(3)


""" --------------Length, Dimensionality, and Shape---------------
Uzunluk, Boyutluluk ve Şekil
:numref:sec_ndarray'deki bazı kavramları tekrar gözden geçirelim. 
Bir vektör sadece bir sayı dizisidir. Ve her dizinin bir uzunluğu olduğu gibi, her vektörün de bir uzunluğu vardır. 
Matematik gösteriminde, bir x vektörünün n gerçek değerli skalerden oluştuğunu söylemek istiyorsak, bunu x∈Rn olarak ifade edebiliriz. 
Bir vektörün uzunluğu genellikle vektörün boyutu olarak adlandırılır.

Sıradan bir Python dizisinde olduğu gibi, Python'un yerleşik len() işlevini çağırarak [bir tensörün uzunluğuna erişebiliriz]. """
print('\n',len(x)) 
# 4

print ('\n',x.shape) 
# torch.Size([4]) 4 elemanlı bir vektör olduğunu gösterir

""" "Boyut" kelimesinin bu bağlamlarda aşırı yüklenme eğiliminde olduğunu ve bunun insanların kafasını karıştırma eğiliminde olduğunu unutmayın. 
Açıklığa kavuşturmak için, bir vektörün veya bir eksenin boyutsallığını, uzunluğuna, yani bir vektörün veya bir eksenin eleman sayısına atıfta bulunmak için kullanırız. 
Bununla birlikte, bir tensörün sahip olduğu eksen sayısına atıfta bulunmak için bir tensörün boyutsallığını kullanırız. 
Bu anlamda, bir tensörün bazı eksenlerinin boyutsallığı, o eksenin uzunluğu olacaktır. """



""" --------------Matrisler-------------------
Vektörlerin skalerleri sıfırdan birinciye genelleştirmesi gibi, matrisler de vektörleri birinciden ikinciye genelleştirir. 
Tipik olarak kalın, büyük harflerle (örneğin, X , Y ve Z ) göstereceğimiz matrisler, kodda iki eksenli tensörler olarak temsil edilir.

Matematik gösteriminde, A matrisinin gerçek değerli skalerden m satır ve n sütundan oluştuğunu ifade etmek için A∈Rm×n kullanırız. 
Görsel olarak, herhangi bir A∈Rm×n matrisini, her bir aij öğesinin i'inci satıra ve j'inci sütuna ait olduğu bir tablo olarak gösterebiliriz:

A = [[a11, a12, ..., a1n], [a21, a22, ..., a2n], ..., [am1, am2, ..., amn]]

Herhangi bir A∈Rm×n için, A'nın şekli ( m , n ) veya m×n'dir. 
Spesifik olarak, bir matris aynı sayıda satır ve sütuna sahip olduğunda şekli kare olur; bu nedenle kare matris olarak adlandırılır.

Bir tensörü başlatmak için en sevdiğimiz işlevlerden herhangi birini çağırırken m ve n olmak üzere iki bileşenli bir şekil belirterek [bir m×n matrisi oluşturabiliriz]."""


A = torch.arange(20).reshape(5, 4) # 0 dan 19 a kadar 20 tensor oluşturuldu ve 5 satır 4 sütunlu bir matris haline getirildi
print('\n',A)

""" tensor([[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11],
        [12, 13, 14, 15],
        [16, 17, 18, 19]]) """


""":eqref:eq_matrix_def'deki bir A matrisinin aij skaler öğesine, [A]ij gibi satır ( i ) ve sütun ( j ) için indeksler belirterek erişebiliriz. 
A matrisinin skaler öğeleri, örneğin :eqref:eq_matrix_def'de verilmediğinde, [A]ij'ye başvurmak için A matrisinin küçük harfini aij dizin alt simgesiyle kullanabiliriz. 
Gösterimi basit tutmak için, a2,3j ve [A]2i−1,3 gibi yalnızca gerektiğinde ayrı dizinlere virgül eklenir.

Bazen eksenleri çevirmek isteriz. Bir matrisin satırlarını ve sütunlarını değiştirdiğimizde, sonuca matrisin devrik denir. 
Resmi olarak, bir A matrisinin A⊤ ile devriğini belirtiriz ve eğer B=A⊤ ise, herhangi bir i ve j için bij=aji olur. 
Bu nedenle, A'nın :eqref:eq_matrix_def içindeki devrik bir n×m matrisidir:


A⊤ = [[a11, a21, ..., am1],[a12, a22, ..., am2],...,[a1n, a2n, ..., amn]]

Şimdi kodda bir (matris devrik) erişiyoruz. """

print('\n',A.T)
""" tensor([[ 0,  4,  8, 12, 16],
        [ 1,  5,  9, 13, 17],
        [ 2,  6, 10, 14, 18],
        [ 3,  7, 11, 15, 19]])"""

""" Matrisler yararlı veri yapılarıdır: farklı varyasyon yöntemlerine sahip verileri düzenlememize izin verirler. 
Örneğin, matrisimizdeki satırlar farklı evlere (veri örnekleri) karşılık gelirken, sütunlar farklı niteliklere karşılık gelebilir. 
Daha önce elektronik tablo yazılımı kullandıysanız veya :numref:sec_pandas'ı okuduysanız, bu size tanıdık gelecektir. 
Bu nedenle, tek bir vektörün varsayılan oryantasyonu bir sütun vektörü olsa da, bir tablo veri setini temsil eden bir matriste, 
her veri örneğini matriste bir satır vektörü olarak ele almak daha gelenekseldir. Ve sonraki bölümlerde göreceğimiz gibi, 
bu sözleşme ortak derin öğrenme uygulamalarını mümkün kılacaktır. Örneğin, bir tensörün en dış ekseni boyunca, 
veri örneklerinin mini kümelerine veya mini küme yoksa yalnızca veri örneklerine erişebilir veya bunları sıralayabiliriz. """




""" --------------Tensörler-------------------
Tıpkı vektörlerin skaleri genelleştirmesi ve matrislerin vektörleri genelleştirmesi gibi, daha da fazla eksene sahip veri yapıları oluşturabiliriz. 
[Tensörler] (bu alt bölümdeki "tensörler" cebirsel nesneleri ifade eder) 
(bize rasgele sayıda eksene sahip n-boyutlu dizileri tanımlamanın genel bir yolunu verir.) 
Örneğin, vektörler birinci dereceden tensörlerdir ve matrisler ikinci derecedendir -düzen tensörleri. 
Tensörler, özel bir yazı tipi yüzünün (örneğin, X, Y ve Z) büyük harfleriyle gösterilir ve indeksleme mekanizmaları 
(örneğin, xijk ve [X]1,2i−1,3) matrislerinkine benzer.

Yüksekliğe, genişliğe karşılık gelen 3 eksen ve renk kanallarını (kırmızı, yeşil ve mavi) 
istiflemek için bir kanal ekseni ile n boyutlu diziler olarak gelen görüntülerle çalışmaya 
başladığımızda tensörler daha önemli hale gelecektir. Şimdilik, daha yüksek dereceli tensörleri atlayacağız ve temellere odaklanacağız."""

X = torch.arange(24).reshape(2, 3, 4) # 0 dan 23 e kadar 24 tensor oluşturuldu ve 2 satır 3 sütunlu 4 derinlikli bir matris haline getirildi
print('\n',X)

""" tensor([[[ 0,  1,  2,  3],
         [ 4,  5,  6,  7],
         [ 8,  9, 10, 11]],

        [[12, 13, 14, 15],
         [16, 17, 18, 19],
         [20, 21, 22, 23]]]) """

A = torch.arange(20, dtype=torch.float32).reshape(5, 4) # 20 den 39 a kadar 20 tensor oluşturuldu ve 5 satır 4 sütunlu bir matris haline getirildi
B = A.clone()  # A matrisinin kopyası oluşturuldu
print('\n',A,A+B)
""" tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.],
        [12., 13., 14., 15.],
        [16., 17., 18., 19.]]) tensor([[ 0.,  2.,  4.,  6.],
        [ 8., 10., 12., 14.],
        [16., 18., 20., 22.],
        [24., 26., 28., 30.],
        [32., 34., 36., 38.]])"""

print ('\n',A*B) # A ve B matrislerinin çarpımı
""" tensor([[  0.,   1.,   4.,   9.],
        [ 16.,  25.,  36.,  49.],
        [ 64.,  81., 100., 121.],
        [144., 169., 196., 225.],
        [256., 289., 324., 361.]])"""
print('\n')
a = 2
X = torch.arange(24).reshape(2, 3, 4)
print('\n',a + X, (a * X).shape) # a ve X matrislerinin toplamı ve çarpımı
""" tensor([[[ 2,  3,  4,  5],
         [ 6,  7,  8,  9],
         [10, 11, 12, 13]],

        [[14, 15, 16, 17],
         [18, 19, 20, 21],
         [22, 23, 24, 25]]]) torch.Size([2, 3, 4])"""

print ('\n',A.sum(axis=[0, 1])) # A matrisinin 0 ve 1 eksenlerindeki toplamı
# tensor(190.)

print('\n',A.mean(), A.sum() / A.numel()) # A matrisinin ortalaması, A matrisinin toplamı ve A matrisinin eleman sayısının bölümü
# tensor(9.5000) tensor(9.5000)

print('\n',A.mean(axis=0), A.sum(axis=0) / A.shape[0]) # A matrisinin 0 eksenindeki ortalaması, A matrisinin 0 eksenindeki toplamı ve A matrisinin 0 eksenindeki eleman sayısının bölümü
# tensor([ 8.,  9., 10., 11.]) tensor([ 8.,  9., 10., 11.])




"""Matrix-Matrix Multiplication
Nokta çarpımları ve matris-vektör çarpımlarını öğrendiyseniz, o zaman matris-matris çarpımı basit olmalıdır.

A∈Rn×k ve B∈Rk×m olmak üzere iki matrisimiz olduğunu varsayalım:
        A=[a11,a12,…,a1k,     B=[b11,b12,…,b1m,
           a21,a22,…,a2k,        b21,b22,…,b2m,
                 …,                  …,  
           an1,an2,…,ank]        bm1,bm2,…,bmm]

A matrisinin i. satırını temsil eden satır vektörünü a⊤i∈Rk ile gösterin ve bj∈Rk, B matrisinin j. sütunundan sütun vektörü olsun.
 C=AB matris çarpımını üretmek için, A'yı satır vektörleri cinsinden ve B'yi sütun vektörleri cinsinden düşünmek en kolayıdır:
 A=[a^T_1, a^T_2, ..., a^T_n] ve B=[b_1, b_2, ..., b_m].

 Daha sonra, her cij elemanını a⊤ibj nokta çarpımı olarak basitçe hesapladığımız için C∈Rn×m matris ürünü üretilir:

[AB matris-matris çarpımını basitçe m matris-vektör çarpımını gerçekleştirmek ve sonuçları bir n×m matris oluşturmak için birleştirmek olarak düşünebiliriz.] 
Aşağıdaki parçada, A ve B üzerinde matris çarpımı gerçekleştiriyoruz. Burada, A 5 satır ve 4 sütundan oluşan bir matris ve B, 4 satır ve 3 sütundan oluşan bir matristir. 
Çarpma işleminden sonra 5 satır ve 3 sütunlu bir matris elde ederiz. """

B = torch.ones(4, 3) # 4 satır 3 sütunlu bir matris oluşturuldu
print('\n',torch.mm(A, B)) # A ve B matrislerinin çarpımı
""" tensor([[ 6.,  6.,  6.],
           [22., 22., 22.],
           [38., 38., 38.],
           [54., 54., 54.],
           [70., 70., 70.]])"""