;Se crea una varible que se llama dato
; el 0x21 es la posicion en donde se almacena
; 0x21 proposito general

;CONFIGURACION
DATO EQU 0x21
;INICIO DE PROGRAMA
	ORG	0X00
	GOTO	START
;CODIGO
START
	BSF	STATUS,5
	CLRF	TRISB
	BCF	STATUS, RP0
	BCF	STATUS,5
	MOVLW	0X00
	MOVWF	PORTB
	GOTO	MENU
MENU
	BTFSC	PORTD, 7 ;RD7
	GOTO	IZQUIERDO ;1
	GOTO	DERECHO ;0
	GOTO	MENU
MV
	MOVF	DATO, W
	MOVWF	PORTB
	RETURN
IZQUIERDO
	MOVLW	B'11111111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11111110'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11111101'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11111011'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11110111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11101111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11011111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'10111111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'01111111'
	MOVWF	DATO
	CALL	MV
	GOTO	MENU
DERECHO
	MOVLW	B'01111111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'10111111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11011111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11101111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11110111'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11111011'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11111101'
	MOVWF	DATO
	CALL	MV

	MOVLW	B'11111110'
	MOVWF	DATO
	CALL	MV
	GOTO 	MENU
END
