import numpy as np
import matplotlib.pyplot as plt

# Parametreleri tanımlama
A = np.random.uniform(2, 2.1)  # 2'den büyük (eşit değil)
B = np.random.uniform(0, 4)  # 4'den küçük (eşit değil)
f1 = 2  # Hz
f2 = 10  # Hz
t_max = 10  # s
fs = 100  # Hz

# Zaman dizisi tanımlama
n_samples = t_max * fs
t = np.linspace(0, t_max, n_samples, endpoint=False)

# Y değerlerini hesaplama
y = A * np.sin(2*np.pi*f1*t) + B * np.cos(2*np.pi*f2*t)

# Grafik çizme
plt.plot(t, y)
plt.xlabel('Zaman (s)')
plt.ylabel('y')
plt.show()