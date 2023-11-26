import torch
"""-----------------Operasyonlar------------------"""
"""
Bu kitap yazılım mühendisliği ile ilgili değildir. 
İlgi alanlarımız sadece dizilerden/dizilere veri okumak ve yazmakla sınırlı değildir. 
Bu diziler üzerinde matematiksel işlemler yapmak istiyoruz. 
En basit ve en yararlı işlemlerden bazıları elementsel işlemlerdir. 
Bunlar, bir dizinin her öğesine standart bir skaler işlem uygular. 
Girdi olarak iki dizi alan işlevler için, öğe bazında işlemler, iki diziden karşılık gelen öğelerin her bir çiftine bazı standart ikili işleçler uygular. 
Bir skaladan skalere eşlenen herhangi bir fonksiyondan elementwise bir fonksiyon yaratabiliriz.

Matematiksel gösterimde, böyle bir tekli skaler operatörü (bir girdi alarak) f:R→R imzasıyla gösterirdik. 
Bu, işlevin herhangi bir gerçek sayıdan ( R ) diğerine eşlendiği anlamına gelir. 
Aynı şekilde, f:R,R→R imzasıyla bir ikili skaler operatörü (iki gerçek girdi alan ve bir çıktı veren) gösteriyoruz. 
Aynı şekle sahip herhangi iki u ve v vektörü ve f ikili operatörü verildiğinde, tüm i için ci←f(ui,vi) ayarlayarak bir c=F(u,v) vektörü üretebiliriz, 
burada ci,ui , ve vi, c,u ve v vektörlerinin i'inci elemanlarıdır. 
Burada, skaler fonksiyonu elementsel bir vektör işlemine yükselterek vektör değerli F:Rd,Rd→Rd'yi ürettik.

Yaygın standart aritmetik işleçlerin (+, -, *, / ve **) tümü, keyfi şekle sahip özdeş şekilli tensörler için elementsel işlemlere kaldırılmıştır. 
Aynı şekle sahip herhangi iki tensör üzerinde elementwise işlemleri çağırabiliriz. 
Aşağıdaki örnekte, 5 öğeli bir demet formüle etmek için virgül kullanıyoruz; burada her öğe, öğe bazında bir işlemin sonucudur.

Operasyonlar
[Yaygın standart aritmetik işleçlerin (+, -, *, / ve ``) tümü, elementsel işlemlere yükseltildi.**]
"""
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2  , 2, 2, 2])
elementwise=x+y, x-y, x*y, x/y, x**y
print('\n',elementwise) # elementwise işlemler
"""
 (tensor([ 3.,  4.,  6., 10.]), 
  tensor([-1.,  0.,  2.,  6.]), 
  tensor([ 2.,  4.,  8., 16.]), 
  tensor([0.5000, 1.0000, 2.0000, 4.0000]), 
  tensor([ 1.,  4., 16., 64.]))
"""

"""
Üs alma gibi tekli işleçler de dahil olmak üzere birçok (eleman bazında daha fazla işlem uygulanabilir).
"""
x = torch.tensor([1.0, 2, 4, 8]) # 1.0, 2, 4, 8 değerlerinden oluşan bir tensor oluşturduk
us=torch.exp(x) # x'in her elemanının üssünü alır
print('\n',us)
"""
tensor([2.7183e+00, 7.3891e+00, 5.4598e+01, 2.9810e+03])
"""


"""
Element bazında hesaplamalara ek olarak, vektör nokta çarpımları ve matris çarpımı da dahil olmak üzere lineer cebir işlemlerini de gerçekleştirebiliriz. 
:numref:sec_linear-cebir'de doğrusal cebirin önemli parçalarını (önceden bilgi sahibi olmadan) açıklayacağız.

Ayrıca daha büyük bir tensör oluşturmak için uçtan uca istifleyerek [birden fazla tensörü bir araya getirebiliriz]. 
Sadece bir tensör listesi sağlamamız ve sisteme hangi eksen boyunca birleştirileceğini söylememiz gerekiyor. 
Aşağıdaki örnek, iki matrisi satırlar (şeklin 0 ekseni, şeklin ilk öğesi) ve sütunlar (eksen 1, şeklin ikinci öğesi) boyunca birleştirdiğimizde ne olduğunu gösterir. 
İlk çıkış tensörünün eksen-0 uzunluğunun ( 6 ), iki giriş tensörünün eksen-0 uzunluklarının ( 3+3 ) toplamı olduğunu görebiliriz; 
ikinci çıkış tensörünün eksen-1 uzunluğu ( 8 ), iki giriş tensörünün eksen-1 uzunluklarının ( 4+4 ) toplamıdır.
"""
X=torch.arange(12, dtype=torch.float32).reshape((3,4))
Y=torch.tensor([[2.0,1,4,3],[1,2,3,4],[4,3,2,1]])
print('\n',torch.cat((X,Y), dim=0), torch.cat((X,Y), dim=1))

""" 
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.],
        [ 2.,  1.,  4.,  3.],
        [ 1.,  2.,  3.,  4.],
        [ 4.,  3.,  2.,  1.]]) 
 tensor([[ 0.,  1.,  2.,  3.,  2.,  1.,  4.,  3.],
        [ 4.,  5.,  6.,  7.,  1.,  2.,  3.,  4.],
        [ 8.,  9., 10., 11.,  4.,  3.,  2.,  1.]])
"""

"""
Bazen, [mantıksal ifadeler aracılığıyla bir ikili tensör oluşturmak] isteriz. Örnek olarak X == Y'yi ele alalım. 
Her konum için, eğer X ve Y o konumda eşitse, yeni tensördeki karşılık gelen giriş 1 değerini alır, 
yani X == Y mantıksal ifadesi o konumda doğrudur; aksi takdirde bu konum 0 alır.
"""
print ('\n',X == Y)
"""
tensor([[False,  True, False,  True],
        [False, False, False, False],
        [False, False, False, False]])
"""

"""
[Tensordaki tüm elemanların toplanması] tek elemanlı bir tensör verir.
"""
print ('\n',X.sum())
"""
tensor(66.)
"""
