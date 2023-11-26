import numpy as np
from scipy.stats import gmean, hmean

n = 10
a = np.random.rand(n) * 2
b = np.random.rand(n) * 2

aritmetik_ortalama_a = np.mean(a)
aritmetik_ortalama_b = np.mean(b)

geometrik_ortalama_a = gmean(a)
geometrik_ortalama_b = gmean(b)

harmonik_ortalama_a = hmean(a)
harmonik_ortalama_b = hmean(b)

karekok_ortalama_a = np.sqrt(np.mean(a**2))
karekok_ortalama_b = np.sqrt(np.mean(b**2))

standart_sapma_a = np.std(a)
standart_sapma_b = np.std(b)

varyans_a = np.var(a)
varyans_b = np.var(b)

iliski_katsayisi = np.corrcoef(a, b)[0,1]

print('a =', a)
print('b =', b)
print('Aritmetik Ortalama a =', aritmetik_ortalama_a)
print('Aritmetik Ortalama b =', aritmetik_ortalama_b)
print('Geometrik Ortalama a =', geometrik_ortalama_a)
print('Geometrik Ortalama b =', geometrik_ortalama_b)
print('Harmonik Ortalama a =', harmonik_ortalama_a)
print('Harmonik Ortalama b =', harmonik_ortalama_b)
print('Karekök Ortalama a =', karekok_ortalama_a)
print('Karekök Ortalama b =', karekok_ortalama_b)
print('Standart Sapma a =', standart_sapma_a)
print('Standart Sapma b =', standart_sapma_b)
print('Varyans a =', varyans_a)
print('Varyans b =', varyans_b)
print('İlişki Katsayısı =', iliski_katsayisi)
