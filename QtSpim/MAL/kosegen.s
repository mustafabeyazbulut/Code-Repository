#Tamsayı kare bir matrisin asal köşegen üzerindeki elemanlarını (satır numarası sütün numarasına eşit olan elemanlar) 1,
#diğer elemanlarını ise -1 yapan bir programı MAL dilinde yazınız. 
#Bu programın veri tanımlamaları sizin için soru4.s dosyasında yapılmıştır. 
#Sizden tanımlı veriler haricinde herhangi başka bir veri tanımlaması yapmamanız istenmektedir.
# Yazdığınız kodu soru4.s dosyasına kaydederek ve QtSpim simülatöründe doğru çalıştığından emin olduktan 
#sonra bu dosya ile birlikte sisteme yükleyiniz. Not: Programdaki  ar ve satir_sutun_sayisi veri tanımlamaları 
#değiştirildiğinde de (örneğin ar: .space 400  satir_sutun_sayisi: 10 ) programınızın doğru çalışması gerekmektedir.


# kare matrisin asal köşegen üzerindeki elemanlarını 1, diğerlerine -1 yapan kod 
.data 
# 4 x 4 lük bir kare matris
ar: 			.space 64
satir_sutun_sayisi:	.word 4

#test icin
string1:    		.asciiz "\n"
string2:    		.asciiz ","

.text
    
main:
        		la 	$s1,ar 				# $s1 registerine Ar dizinin başlangıç adresini atıyorum. Dizinin başlangıç değeri gerekli olduğunda $s1 registerini kullanacağım.
        		la 	$s2,satir_sutun_sayisi 		# $s2 ye satir_sütun sayısının adresini ekliyorum. Bundan sonraki işlemlerde $s2 registerini kullanacağım.
        		lw 	$s2,0($s2)			# lw komutu ile o adresteki değeri $s2 registerine eklemiş olduk

        		jal 	matris				# matris fonksiyonuna gidiyoruz. Bu fonksiyonda matrisin tüm elemanlarını -1 yapacağız.
        		jal 	kosegen				# kosegen fonksiyonuna gidiyoruz.Bu fonksiyonda matrisin kösegen elemanlarını 1 yapacağız.

        		li 	$v0,10				
        		syscall					 

matris: 							
        		li	$t1, -1				# $t1=-1
        		move 	$t2,$s1 			# Matrisin baslangic adresini kayip etmemek icin $t2 ye bu adresi yaziyorum.
        		li 	$t3,0      			# $t3'ü döngü için sayaç olarak kullanacağım. 0'dan başlaması gerekiyor.
        		move 	$t4,$s2    			# $2 de satir sayısı var. Kaybolmasın diye işlemlerimizi $t2 registeri ile yapıyoruz.
        		mul	$t4, $t4, $t4   		# N x N yaparak matrisin eleman sayisini buluyoruz.

while1:    		sw 	$t1,0($t2) 			# t2 nin gosterdigi adresin icerigi -1 oldu.
                	addi	$t3, $t3, 1			# sayac 1 arttırıldı.
                	addi	$t2, $t2, 4    			# her seferde 4 bayt ileri gidiyor.
               		bgt 	$t4, $t3,while1 		# if($t4>$t3) while1'e git. 
        		j	$31  				# return adrese geri donuyor.


kosegen: 							
        		move 	$t1,$s1  			# Dizinin başlangıç adresini kaybetmemek için $t1 registerine atadım.
        		li 	$t2,4       			# $t2 registerine artış miktarını ekliyorum.
        		move 	$t3,$s2   			# satir sayisini $t3 registerine aliyorum. 
        		addi 	$t3,$t3,1			# $t3= satır sayısı + 1 oluyor.
        		mul	$t2, $t2, $t3  			# N x N lik bir matriste köşegenler n*(n+1) şeklinde bulunuyor. $t2 registerinde köşegen adresimlerimizin artış miktarını eklemiş olduk
        		li 	$t4,1				# $t4=1 
        		li 	$t5,0     			# $t5=0 sayac olarak kullanacagim.

while2:			sw 	$t4,0($t1)			# Memory[$t1+0]=$t4 yani 1 değeri atanıyor.
            		add 	$t1,$t1,$t2   			# $t2 de köşegenler için artış miktarımız bulunuyor. Her köşegeni n*(n+1) arttırarak bir sonraki köşegenimizin adresini buluyoruz.
            		addi 	$t5,$t5,1			# sayacı 1 arttırdım.
            		bgt 	$s2,$t5,while2			# if($s2>$t5) while2'ye git. 
        		j	$31				# return adrese geri donuyor.








