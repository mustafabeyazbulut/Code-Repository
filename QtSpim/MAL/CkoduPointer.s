#int x,y;
#int *ptr1,*ptr2;

#x = 88,
#ptr1 = &x;
#ptr2 = &y;
#*ptr2 = *ptr1;



.data
x:  		.word 0
y:  		.word 0
ptr1:   	.word 0
ptr2:   	.word 0

.text

# la $s0,x
# la $s1,ptr1
# la $s2,ptr2
# la $s3,y

main:		#x=88
		la $s0,x			# $s0=x'in adresi yazıldı.
		li $t0,88			# $t0=88
		sw $t0,0($s0)			# (Memory[$s0+0]=$t0) (yani x) = $t0(yani 88) atandı

		#ptr1 = &x;
		la $s1,ptr1			# $s1=ptr1 adresi
		sw $s0,0($s1)			# (Memory[$s1+0]=$s0)  x'in adresi atandı

		#ptr2 = &y;
		la $s2,ptr2			# $s2=ptr2 adresi	
		la $s3,y			# $s3=y adresi
		sw $s3,0($s2)			# (Memory[$s2+0]=$s3) $s2 ptr2 adresine, $s3 yani y'nin adresi atandı

		#*ptr2 = *ptr1
		lw $s2,0($s2)			# ($s2=Memory[$s2+0]) $s2'ye $s2'nin değeri yani y'nin adresi atandı.
		lw $s1,0($s1)			# ($s1=Memory[$s1+0]) $s1'e x'in adresi atandı
		lw $s1,0($s1)			# ($s1=Memory[$s1+0]) 2. çalıştırma da adresteki değer atanmış oldu.
		sw $s1,0($s2)			# (Memory[$s2+0]=$s1) *ptr2=*ptr1 


        	li $v0,10
        	syscall
