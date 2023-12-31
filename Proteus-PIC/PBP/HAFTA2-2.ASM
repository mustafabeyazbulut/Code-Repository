
; PICBASIC PRO(TM) Compiler 2.60, (c) 1998, 2009 microEngineering Labs, Inc. All Rights Reserved. 
_USED			EQU	1

	INCLUDE	"C:\PBP\16F877.INC"


; Define statements.
; C:\PBP\16F877.BAS        	00018	DEFINE  CODE_SIZE 8
#define		CODE_SIZE		 8

RAM_START       		EQU	00020h
RAM_END         		EQU	001EFh
RAM_BANKS       		EQU	00004h
BANK0_START     		EQU	00020h
BANK0_END       		EQU	0007Fh
BANK1_START     		EQU	000A0h
BANK1_END       		EQU	000EFh
BANK2_START     		EQU	00110h
BANK2_END       		EQU	0016Fh
BANK3_START     		EQU	00190h
BANK3_END       		EQU	001EFh
EEPROM_START    		EQU	02100h
EEPROM_END      		EQU	021FFh

; C:\PBP\PBPPIC14.RAM      	00012	A00020	R0      VAR     WORD BANK0 SYSTEM       ' System Register
R0              		EQU	RAM_START + 000h
; C:\PBP\PBPPIC14.RAM      	00013	A00022	R1      VAR     WORD BANK0 SYSTEM       ' System Register
R1              		EQU	RAM_START + 002h
; C:\PBP\PBPPIC14.RAM      	00014	A00024	R2      VAR     WORD BANK0 SYSTEM       ' System Register
R2              		EQU	RAM_START + 004h
; C:\PBP\PBPPIC14.RAM      	00015	A00026	R3      VAR     WORD BANK0 SYSTEM       ' System Register
R3              		EQU	RAM_START + 006h
; C:\PBP\PBPPIC14.RAM      	00016	A00028	R4      VAR     WORD BANK0 SYSTEM       ' System Register
R4              		EQU	RAM_START + 008h
; C:\PBP\PBPPIC14.RAM      	00017	A0002A	R5      VAR     WORD BANK0 SYSTEM       ' System Register
R5              		EQU	RAM_START + 00Ah
; C:\PBP\PBPPIC14.RAM      	00018	A0002C	R6      VAR     WORD BANK0 SYSTEM       ' System Register
R6              		EQU	RAM_START + 00Ch
; C:\PBP\PBPPIC14.RAM      	00019	A0002E	R7      VAR     WORD BANK0 SYSTEM       ' System Register
R7              		EQU	RAM_START + 00Eh
; C:\PBP\PBPPIC14.RAM      	00020	A00030	R8      VAR     WORD BANK0 SYSTEM       ' System Register
R8              		EQU	RAM_START + 010h
; C:\PBP\PBPPIC14.RAM      	00026	A00032	FLAGS   VAR     BYTE BANK0 SYSTEM       ' Static flags
FLAGS           		EQU	RAM_START + 012h
; C:\PBP\PBPPIC14.RAM      	00025	A00033	GOP     VAR     BYTE BANK0 SYSTEM       ' Gen Op Parameter
GOP             		EQU	RAM_START + 013h
; C:\PBP\PBPPIC14.RAM      	00022	A00034	RM1     VAR     BYTE BANK0 SYSTEM       ' Pin 1 Mask
RM1             		EQU	RAM_START + 014h
; C:\PBP\PBPPIC14.RAM      	00024	A00035	RM2     VAR     BYTE BANK0 SYSTEM       ' Pin 2 Mask
RM2             		EQU	RAM_START + 015h
; C:\PBP\PBPPIC14.RAM      	00021	A00036	RR1     VAR     BYTE BANK0 SYSTEM       ' Pin 1 Register
RR1             		EQU	RAM_START + 016h
; C:\PBP\PBPPIC14.RAM      	00023	A00037	RR2     VAR     BYTE BANK0 SYSTEM       ' Pin 2 Register
RR2             		EQU	RAM_START + 017h
; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00014	A00038	i var byte
_i               		EQU	RAM_START + 018h
; C:\PBP\16F877.BAS        	00022	PORTL   VAR     PORTB
_PORTL           		EQU	 PORTB
; C:\PBP\16F877.BAS        	00023	PORTH   VAR     PORTC
_PORTH           		EQU	 PORTC
; C:\PBP\16F877.BAS        	00024	TRISL   VAR     TRISB
_TRISL           		EQU	 TRISB
; C:\PBP\16F877.BAS        	00025	TRISH   VAR     TRISC
_TRISH           		EQU	 TRISC
#define _button1         	_PORTB??7
#define _PORTB??7        	 PORTB, 007h
	INCLUDE	"HAFTA2-2.MAC"
	INCLUDE	"C:\PBP\PBPPIC14.LIB"


; C:\PBP\16F877.BAS        	00012	BANK0   $0020, $007F
; C:\PBP\16F877.BAS        	00013	BANK1   $00A0, $00EF
; C:\PBP\16F877.BAS        	00014	BANK2   $0110, $016F
; C:\PBP\16F877.BAS        	00015	BANK3   $0190, $01EF
; C:\PBP\16F877.BAS        	00016	EEPROM  $2100, $21FF
; C:\PBP\16F877.BAS        	00017	LIBRARY "PBPPIC14"
; C:\PBP\16F877.BAS        	00018	DEFINE  CODE_SIZE 8

; C:\PBP\16F877.BAS        	00020	        include "PIC14EXT.BAS"

; C:\PBP\16F877.BAS        	00027	        include "PBPPIC14.RAM"

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00002	TRISB=%10000000 
	MOVE?CB	080h, TRISB

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00006	PORTB=0  'Biz buna ��k�� portunutemizlemediyoruz.E�erbunu yapmazsak daha �nceden akl�nda kalan bilgiye g�re ilk �al��t�rmada LEDlerin baz�lar� yanar baz�lar� s�ner
	MOVE?CB	000h, PORTB
; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00007	SYMBOL button1=PORTB.7

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00016	label:

	LABEL?L	_label	

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00017	while button1=1
	LABEL?L	L00001	
	CMPNE?TCL	_button1, 001h, L00002

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00018	i=i+1
	ADD?BCB	_i, 001h, _i

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00019	portb=i:PAUSE 100    ': koyarsak yan yana kod yazabiliriz.
	MOVE?BB	_i, PORTB

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00019	portb=i:PAUSE 100    ': koyarsak yan yana kod yazabiliriz.
	PAUSE?C	064h

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00020	wend
	GOTO?L	L00001
	LABEL?L	L00002	

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00022	portb=0
	MOVE?CB	000h, PORTB

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00023	i=0
	MOVE?CB	000h, _i

; C:\USERS\MUSTAFA\DOCUMENTS\GITHUB\PROTEUS\PBP\HAFTA2-2.PBP	00024	goto label
	GOTO?L	_label

	END
