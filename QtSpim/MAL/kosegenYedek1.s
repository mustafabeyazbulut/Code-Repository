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
        		la 	$s1,ar 				# $1 registerine Ar dizinin başlangıç adresini atıyorum.
        		la 	$s2,satir_sutun_sayisi 		# dizinin eleman sayisi degisken olabilecegi icin kayit ediyorum.
        		lw 	$s2,0($s2)

        		jal 	elemanlari_eksile
        		jal 	koseleri_birle

        		jal 	test
        		li 	$v0,10
        		syscall

elemanlari_eksile: 						#Bu fonksiyon dizin tüm elemanlarini -1 yapmaktadir.
        		li	$t1, -1
        		move 	$t2,$s1 			#Dizin baslangic adresini kayip etmemek icin $t2 ye bu adresi yaziyorum.
        		li 	$t3,0      			#$t2 4 bayt olarak ilerletecegim icin $t3 count gibi kullaniyorum.
        		move 	$t4,$s2    			#sinir degeri olarak kullanacagim.
        		mul	$t4, $t4, $t4   		#satir sayisini kendisiyle carpiyorum 4*4 = 16 kez donguye girmesi gerekir ilk ornek icin

eksile:    		sw 	$t1,0($t2) 			#t2 nin gosterdigi adresin icerigi -1 oldu.
                	addi	$t3, $t3, 1
                	addi	$t2, $t2, 4    			#her seferde 4 bayt ileri gidiyor.
               		bgt 	$t4, $t3,eksile 		#kac eleman varsa o kadar donguye giriyor.
        		j	$31  				# return adrese geri donuyor.


koseleri_birle: 						# köşegen üzerindeki elemanlarını 1 yapmak için kullanıyorum.
        		move 	$t1,$s1  			#dizin adresini aliyorum.
        		li 	$t2,4       			#her seferindeki artis miktari hesaplaniyor.
        		move 	$t3,$s2   			# satir sayisini aliyorum.
        		addi 	$t3,$t3,1
        		mul	$t2, $t2, $t3  			#t2*t3 ile kosegenlerin adreslerini bulacagimiz sayiyi bulduk.
        		li 	$t4,1
        		li 	$t5,0     			#sayac olarak kullanacagim deger

birle: 			sw 	$t4,0($t1)
            		add 	$t1,$t1,$t2   			#bu sekilde her seferinde kosegenleri bularak onlari bir yapiyoruz.
            		addi 	$t5,$t5,1
            		bgt 	$s2,$t5,birle
        		j	$31

test:    							#Bu kodun amacı olusan degerleri ekrana tek tek dizi seklinde yazip kodun dogrulugunu anlamaktir.
        		move 	$t1,$s1  			#t1 icerisine arr dizisinin ilk elemanini koydum.
        		li 	$t2,0
        		move 	$t3,$s2    			#sinir degeri olarak kullanacagim.
        		mul	$t3, $t3, $t3   		#satir sayisini kendisiyle carpiyorum 4*4 = 16 kez donguye girmesi gerekir ilk ornek icin

yazdir:     
			li 	$v0, 1			    	#print integer
                    	lw 	$t4,0($t1)
                    	move 	$a0, $t4  
                    	syscall
                    	addi 	$t2, $t2,1 
                    	addi 	$t1,$t1,4
                    	div 	$t2,$s2  			#t2 yi eleman sayisina boluyorum bu sayede tam bolundugu zaman degerleri boyutuna uygun yazdirmis olacagim.
                    	mfhi 	$s4   				#s4 kalani koyuyorum.
                    	li 	$v0 , 4				#yazdir string1 
                    	la 	$a0 , string2      		#degerler karismasin diye virgul ile ayriliyor.  
                    	syscall
                    	bne	$s4,$0,yazma
                    	li 	$v0 , 4				#yazdir string1 
                    	la 	$a0 , string1  
                    	syscall

yazma : 
                        bgt 	$t3,$t2,yazdir
        		j	$31 			 	# return adrese geri donuyor.







