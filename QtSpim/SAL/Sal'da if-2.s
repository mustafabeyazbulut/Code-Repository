 .data
A:		.word	-15
BB:		.word	2
C:		.word   0
temp:	.word	0

.text
__start:   bgtz    A, ifpart
	       mul     temp, BB, BB
	       add     C, temp, 12
		   b       endif   
ifpart:	   mul     temp, 2, BB
	       add     C, temp, 4
endif:
