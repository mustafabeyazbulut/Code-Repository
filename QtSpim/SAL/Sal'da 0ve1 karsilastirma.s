		.data
x:			.word	0x325238A8
temp:		.word   0	
counter:	.word 	0
kalan:		.word	0
count1:		.word	0
count0:		.word	0
string1:	.asciiz "az!\n"
string2: 	.asciiz "fazla!\n"
string3: 	.asciiz "esit!\n"

		.text

__start:   
whiles:				bgt counter,32,endwhile		# if (counter > 32) goto endwhile (32 Bitin tamamini kontrol ettiyse donguden cik)
					beq x,0,endwhile			# if (x == 0) goto endwhile (sayimiz 0 a esit olursa donguye devam etmesine gerek yoktur)
					rem kalan,x,2				# 2 ye bolumunden sonra 0 mi 1 mi kaldigina bakariz. bunu kalan degiskenine atariz.
					div x,x,2					# x degiskeninde bulunan sayiyi 2 ye boleriz
					add counter,counter,1		# while dongusu icin sayac degiskenini 1 arttiririz.
					beq kalan,1,bir				# if (kalan == 1) goto label
					beq kalan,0,zero			# if (kalan == 0) goto label
					b whiles
					
bir:				add count1,count1,1			# count1 degiskenini 1 arttiririz.
					b whiles					# donguye geri doneriz
zero:				add count0,count0,1			# count0 degiskenini 1 arttiririz.
					b whiles					# donguye geri doneriz

endwhile:			blt count0,count1,az		# if (count0 < count1) goto az
					bgt count0,count1,fazla		# if (count0 > count1) goto fazla
					puts string3				# ekrana string3u yazdirir
					b bitir

az:					puts string1				# ekrana string1 i yazdirir
					b bitir
					
fazla:				puts string2				# ekrana string2 i yazdirir
bitir: