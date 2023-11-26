"""
(Başlamak için, torch'u içe aktarıyoruz. PyTorch olarak adlandırılsa da, pytorch yerine torch'u içe aktarmamız gerektiğini unutmayın.)
"""
import torch


"""
[Bir tensör, sayısal değerlerin (muhtemelen çok boyutlu) bir dizisini temsil eder.] 
Tek eksenli tensöre vektör denir. 
İki eksenli bir tensöre matris denir. 
k>2 eksenleri ile özel adları bırakırız ve nesneye sadece k'inci dereceden bir tensör olarak başvururuz.
"""

"""
PyTorch, değerlerle önceden doldurulmuş yeni tensörler oluşturmak için çeşitli işlevler sağlar. 
Örneğin, arange(n)'yi çağırarak, 0'dan (dahil) başlayıp n'de (dahil değil) biten, eşit aralıklı değerlerden oluşan bir vektör oluşturabiliriz. 
Varsayılan olarak, aralık boyutu 1'dir. Aksi belirtilmedikçe, yeni tensörler ana bellekte depolanır ve CPU tabanlı hesaplama için belirlenir.
"""
x = torch.arange(12, dtype=torch.float32) # 0'dan 11'e kadar 12 elemanlı bir tensor oluşturduk
print(x)
""" tensor([ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10., 11.]) """



"""
(Bir tensörün şekline) (ve toplam eleman sayısına) (her eksen boyunca uzunluk) şekil özelliğini inceleyerek erişebiliriz.
"""
print('\n',x.shape) # tensorun boyutunu verir """  torch.Size([12]) """


"""
Bir tensördeki elemanların toplam sayısını, yani tüm şekil elemanlarının çarpımını bilmek istiyorsak boyutunu inceleyebiliriz. 
Burada bir vektörle uğraştığımız için, şeklinin tek elemanı boyutuyla aynıdır.
"""
print("\nNumel Kodu : ",x.numel()) # tensorun eleman sayısını verir """ Numel Kodu :  12 """


"""
[Öğe sayısını veya değerlerini değiştirmeden bir tensörün şeklini değiştirmek] için yeniden şekillendirme işlevini çağırabiliriz. 
Örneğin, x tensörümüzü (12,) şeklindeki bir satır vektöründen (3, 4) şeklindeki bir matrise dönüştürebiliriz. 
Bu yeni tensör, tamamen aynı değerleri içerir, ancak bunları 3 satır ve 4 sütun olarak düzenlenmiş bir matris olarak görüntüler. 
Yinelemek gerekirse, şekil değişse de unsurlar değişmedi. Yeniden şekillendirme ile boyutun değişmediğini unutmayın.
"""
X = x.reshape(3, 4) # tensoru 3 satır 4 sütunlu bir matrise dönüştürdük
print('\n',X)
"""
 tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.]])
"""



"""
Her boyutu manuel olarak belirterek yeniden şekillendirmeye gerek yoktur. 
Hedef şeklimiz, şekli (yükseklik, genişlik) olan bir matris ise, genişliği öğrendikten sonra, yükseklik dolaylı olarak verilir. 
Bölmeyi neden kendimiz yapmak zorundayız? 
Yukarıdaki örnekte 3 satırlı bir matris elde etmek için hem 3 satır hem de 4 sütun olması gerektiğini belirtmiştik. 
Neyse ki tensörler, geri kalanı verilen bir boyutu otomatik olarak çözebilir. 
Tensörlerin otomatik olarak çıkarım yapmasını istediğimiz boyuta -1 koyarak bu yeteneği çağırıyoruz. 
Bizim durumumuzda, x.reshape(3, 4) çağırmak yerine, x.reshape(-1, 4) veya x.reshape(3, -1) olarak adlandırabilirdik.

Tipik olarak, matrislerimizin ya sıfırlar, birler, diğer bazı sabitler ya da belirli bir dağılımdan rastgele örneklenmiş sayılarla başlatılmasını isteyeceğiz. 
[Tüm öğeleri 0'a ayarlı] (veya 1) ve (2, 3, 4) şeklinde bir tensörü temsil eden bir tensör oluşturabiliriz:
"""
zereos = torch.zeros((2, 3, 4)) # 2 tane 3 satırlı 4 sütunlu sıfırlardan oluşan bir tensor oluşturduk
print('\n',zereos)
"""
 tensor([[[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]],

        [[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]]])
"""



"""
Benzer şekilde, her eleman 1'e ayarlı tensörleri aşağıdaki gibi oluşturabiliriz:
"""
ones = torch.ones((2, 3, 4)) # 2 tane 3 satırlı 4 sütunlu birlerden oluşan bir tensor oluşturduk
print('\n',ones)
"""
 tensor([[[1., 1., 1., 1.],
         [1., 1., 1., 1.],
         [1., 1., 1., 1.]],

        [[1., 1., 1., 1.],
         [1., 1., 1., 1.],
         [1., 1., 1., 1.]]])
"""


"""
Çoğu zaman, bazı olasılık dağılımlarından [bir tensördeki her öğe için değerleri rastgele örneklemek] isteriz.
Örneğin, bir sinir ağında parametre olarak hizmet verecek diziler oluşturduğumuzda, tipik olarak değerlerini rastgele başlatırız. 
Aşağıdaki parçacığı (3, 4) şeklinde bir tensör oluşturur. 
Öğelerinin her biri, ortalaması 0 ve standart sapması 1 olan standart bir Gauss (normal) dağılımından rastgele örneklenir.
"""
randn = torch.randn(3, 4) # 3 satırlı 4 sütunlu rastgele değerlerden oluşan bir tensor oluşturduk
print('\n',randn)
"""
 tensor([[ 1.6893,  1.2158, -0.7881, -1.7904],
        [-0.5688,  0.2818, -2.0892,  0.0818],
        [ 0.3213, -1.0058,  0.0851, -0.5216]])
"""


"""
Ayrıca, sayısal değerleri içeren bir Python listesi (veya listeler listesi) sağlayarak istenen tensörde [her öğe için tam değerleri belirtebiliriz]. 
Burada, en dıştaki liste eksen 0'a ve iç liste eksen 1'e karşılık gelir.
"""
tensor= torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]]) # 3 satırlı 4 sütunlu tensor oluşturduk
print('\n',tensor)
"""
 tensor([[2, 1, 4, 3],
        [1, 2, 3, 4],
        [4, 3, 2, 1]])
"""

