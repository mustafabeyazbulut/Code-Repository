 .data
a:		.word	
bb:		.word	
c:		.word   
temp:	.word   	
	


.text

__start:   blez    a, ifpart
	       mul     temp, 2, bb
	       add     c, temp, 4
	       b       endif
ifpart:	   mul     temp, bb, bb
	       add     c, temp, 12
endif: