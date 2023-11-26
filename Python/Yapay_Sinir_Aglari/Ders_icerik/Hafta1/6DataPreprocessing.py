"""--------------Data Preprocessing-------------------"""

"""--------------Veri Ön İşleme-------------------------
:etiket:sec_pandalar

Şimdiye kadar, zaten tensörlerde depolanan verileri işlemek için çeşitli teknikler tanıttık. 
Derin öğrenmeyi gerçek dünya problemlerini çözmeye uygulamak için, 
tensör formatında güzelce hazırlanmış veriler yerine genellikle ham verileri önceden işlemekle başlarız. 
Python'daki popüler veri analizi araçları arasında yaygın olarak pandas paketi kullanılır. 
Geniş Python ekosistemindeki diğer birçok uzantı paketi gibi pandalar da tensörlerle birlikte çalışabilir. 
Bu nedenle, ham verileri pandalarla önceden işlemek ve bunları tensör formatına dönüştürmek için kısaca adımlar atacağız. 
Daha sonraki bölümlerde daha fazla veri ön işleme tekniğini ele alacağız.
"""




"""-----------------Veri Kümesini Okumak - Reading the Dataset-------------------
Örnek olarak (bir csv (virgülle ayrılmış değerler) dosyasında depolanan yapay bir veri kümesi oluşturarak) ../data/house_tiny.csv ile başlıyoruz. 
Diğer formatlarda saklanan veriler benzer şekillerde işlenebilir.

Aşağıda veri setini satır satır bir csv dosyasına yazıyoruz.
"""

import os # işletim sistemi

os.makedirs(os.path.join('.', 'data'), exist_ok=True)  # Create a path `../data`
data_file = os.path.join('.', 'data', 'house_tiny.csv') # Create a path `../data/house_tiny.csv`
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n') # column names
    f.write('NA,Pave,127500\n')  # 
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')


import pandas as pd

data = pd.read_csv(data_file)
print(data)
"""
   NumRooms Alley   Price
0       NaN  Pave  127500
1       2.0   NaN  106000
2       4.0   NaN  178100
3       NaN   NaN  140000
"""

print (data["Price"].mean()) # ortalama fiyat hesaplandı
"""137900.0"""







"""----------------Handling Missing Data-Eksik verileri işlemek-------------------""" 

"""
"NaN" girişlerinin eksik değerler olduğunu unutmayın. 
Eksik verileri işlemek için, tipik yöntemler, atama ve silmeyi içerir; 
burada atama, eksik değerleri ikame edilenlerle değiştirirken, silme, eksik değerleri yok sayar. 
Burada ithamı ele alacağız.

Tamsayı-konum tabanlı indeksleme (iloc) ile, verileri girişlere ve çıkışlara böleriz; 
birincisi ilk iki sütunu alırken, ikincisi yalnızca son sütunu tutar. 
Eksik girdilerdeki sayısal değerler için ["NaN" girişlerini aynı sütunun ortalama değeriyle değiştiririz.]
"""

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2] 
inputs = inputs.fillna(inputs.mean()) 
print(inputs)

"""
 FutureWarning: DataFrame.mean içindeki sayısal_only varsayılan değeri kullanımdan kaldırılmıştır. 
 Gelecekteki bir sürümde, varsayılan olarak False olacaktır. Ayrıca, 'numeric_only=None' belirtmek kullanımdan kaldırılmıştır. 
 Bu uyarıyı susturmak için yalnızca geçerli sütunları seçin veya sayısal_only değerini belirtin.
   NumRooms Alley
0       3.0  Pave
1       2.0   NaN
2       4.0   NaN
3       3.0   NaN
"""

"""
[Girişlerdeki kategorik veya ayrık değerler için, kategori olarak "NaN" kabul ediyoruz.] 
"Alley" sütunu yalnızca "Pave" ve "NaN" olmak üzere iki tür kategorik değer aldığından, 
pandalar bu sütunu otomatik olarak iki sütuna dönüştürebilir " Alley_Pave" ve "Alley_nan". Alley tipi "Pave" olan bir satır, 
"Alley_Pave" ve "Alley_nan" değerlerini 1 ve 0 olarak ayarlayacaktır. Alley tipi eksik olan bir satır, değerlerini 0 ve 1 olarak ayarlayacaktır.
"""

inputs = pd.get_dummies(inputs, dummy_na=True)  # dummy_na=True: NaN değerler için değişkenler oluşturur
print('\n',inputs)
"""
    NumRooms  Alley_Pave  Alley_nan
0       3.0           1          0
1       2.0           0          1
2       4.0           0          1
3       3.0           0          1
"""



"""-------------------Tensör Formatına Dönüştürme------------------
Artık [giriş ve çıkışlardaki tüm girişler sayısaldır, tensör formatına dönüştürülebilirler.] 
Veriler bu formatta olduğunda, :numref:sec_ndarray'de tanıttığımız tensör işlevleriyle daha fazla manipüle edilebilirler.
"""
import torch
X, y = torch.tensor(inputs.values), torch.tensor(outputs.values) # values: Pandas DataFrame'i numpy.ndarray'e dönüştürür
print('\n',X,y)

"""
 tensor([[3., 1., 0.],
        [2., 0., 1.],
        [4., 0., 1.],
        [3., 0., 1.]], dtype=torch.float64) tensor([127500, 106000, 178100, 140000])
"""