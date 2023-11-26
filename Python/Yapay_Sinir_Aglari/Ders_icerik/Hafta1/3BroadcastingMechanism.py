import torch

"""Broadcasting Mechanism"""
"""
:label:subsec_broadcasting

Yukarıdaki bölümde, aynı şekle sahip iki tensör üzerinde elementsel işlemlerin nasıl yapıldığını gördük. 
Belirli koşullar altında, şekiller farklı olsa bile [yayın mekanizmasını çağırarak öğe bazında işlemler gerçekleştirebiliriz.] 
Bu mekanizma şu şekilde çalışır: 
    İlk olarak, öğeleri uygun şekilde kopyalayarak dizilerden birini veya her ikisini genişletin, 
    böylece bu dönüşümden sonra ikisi tensörler aynı şekle sahiptir. 
    İkinci olarak, elde edilen diziler üzerinde elementsel işlemleri gerçekleştirin.

Çoğu durumda, aşağıdaki örnekte olduğu gibi, bir dizinin başlangıçta yalnızca 1 uzunluğa sahip olduğu bir eksen boyunca yayın yaparız:
"""
a = torch.arange(3).reshape((3, 1)) # arange ile 0 dan 2 ye kadar 3 sayı üretildi ve 3 satır 1 sütunluk matrise dönüştürdük
b = torch.arange(2).reshape((1, 2))
print(a , b)   # a ve b matrislerini yazdırdık
"""
tensor([[0],
        [1],
        [2]]) tensor([[0, 1]])
"""

"""
a ve b sırasıyla 3×1 ve 1×2 matris olduğundan, onları toplamak istersek şekilleri eşleşmez. 
Her iki matrisin girişlerini daha büyük bir 3×2 matrise şu şekilde yayınlıyoruz: 
a matrisi için sütunları çoğaltır ve matris b için her ikisini de eleman bazında toplamadan önce satırları çoğaltır.
"""
print(a + b)    # a ve b matrislerini topladık
"""
tensor([[0, 1],
        [1, 2],
        [2, 3]])
"""