import torch
x = torch.arange(12, dtype=torch.float32) # 0 dan 11 e kadar 12 sayı üretildi
X = x.reshape(3, 4) # 3 satırlı 4 sütunlu bir tensor oluşturduk

"""---------------Indexing and Slicing--------------"""
"""
Diğer herhangi bir Python dizisinde olduğu gibi, bir tensördeki öğelere indeks ile erişilebilir. 
Herhangi bir Python dizisinde olduğu gibi, ilk öğenin dizini 0'dır ve aralıklar, ilk öğeyi ancak son öğeden önce içerecek şekilde belirtilir. 
Standart Python listelerinde olduğu gibi, negatif indeksler kullanarak listenin sonuna kadar elemanlara göreceli konumlarına göre erişebiliriz.

Böylece [[-1] son öğeyi seçer ve [1:3] ikinci ve üçüncü öğeleri seçer] aşağıdaki gibi:
"""
print(X)
"""
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.]])
"""



print('\n',X[-1], X[1:3]) # X matrisinin son satırını ve 1. ve 2. satırlarını yazdırdık
"""
tensor([ 8.,  9., 10., 11.]) tensor([[4., 5., 6., 7.],
        [8., 9., 10., 11.]])
"""

X[1, 2] = 9 # X matrisinin 1. satırının 2. sütununu 9 olarak değiştirdik
print ('\n',X) # X matrisinin 1. satırının 2. sütununu 9 olarak değiştirdik
"""
tensor([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  9.,  7.],
        [ 8.,  9., 10., 11.]])
"""
X[0:2, :] = 12 # X matrisinin 0. ve 1. satırlarını 12 olarak değiştirdik
print ('\n',X) 

"""
 tensor([[12., 12., 12., 12.],
        [12., 12., 12., 12.],
        [ 8.,  9., 10., 11.]])
"""
