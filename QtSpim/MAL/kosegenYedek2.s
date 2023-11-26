# kare matrisin asal köşegen üzerindeki elemanlarını 1, diğerlerine -1 yapan kod 
.data 
# 4 x 4 lük bir kare matris
ar: 	.space 64
satir_sutun_sayisi:	.word 4


.text
.globl main
main:	la	$10,satir_sutun_sayisi
	lw	$10,0($10)
	add	$11,$0,$0	#satir no
	add	$12,$0,$0	#sutun no
	la	$14,ar

geri:	mult	$11,$10
	mflo	$15
	add	$15,$15,$12
	sll	$15,$15,2
	add	$15,$15,$14
	li	$17,-1
	sub	$16,$11,$12
	bne	$16,$0,ileri
	li	$17,1

ileri:	sw	$17,0($15)
	addi	$12,$12,1
	sub	$2,$10,$12
	bne	$2,$0,geri	
	addi	$11,$11,1
	add	$12,$0,$0
	sub	$2,$11,$10
	bne	$2,$0,geri

	li $v0, 10
	syscall