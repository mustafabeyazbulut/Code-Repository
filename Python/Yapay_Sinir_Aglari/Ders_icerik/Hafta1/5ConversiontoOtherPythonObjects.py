import torch
x = torch.arange(12, dtype=torch.float32) # 0 dan 11 e kadar 12 sayı üretildi
X = x.reshape(3, 4) # 3 satırlı 4 sütunlu bir tensor oluşturduk

"""--------------Conversion to Other Python Objects-----------------"""
"""
[Bir NumPy tensörüne (ndarray) dönüştürmek] veya tam tersi kolaydır. 
Torç Tensörü ve numpy dizisi, temeldeki bellek konumlarını paylaşacak ve yerinde bir işlemle birini değiştirmek diğerini de değiştirecektir.
"""

A = X.numpy() # X matrisini numpy dizisine dönüştürdük
B = torch.from_numpy(A) # A numpy dizisini tekrar torch dizisine dönüştürdük

print(type(A), type(B)) # A ve B nin tipini yazdırdık

"""<class 'numpy.ndarray'> <class 'torch.Tensor'>"""


"""(1 boyut tensörünü Python skalerine dönüştürmek) için item işlevini veya Python'un yerleşik işlevlerini çağırabiliriz."""
a = torch.tensor([3.5])
print('\n',a, a.item(), float(a), int(a) ) # a matrisini yazdırdık
"""tensor([3.5000]) 3.5 3.5 3"""