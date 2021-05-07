;Configuration

;Inicio de programa
	ORG	0X00 ;origen posicion principal en memoria.
	GOTO 	START ;etiqueta de inicio
;Codigo
START
	BSF	STATUS,5 ;BSF en el estado 5 del status para ir al banco 1
	CLRF	TRISB ;si se coloca en 0 sera salida, 1 es entrada
	BCF	STATUS,RP0 ;este es por nombre
	BCF 	STATUS,5 ;RP0 y 5 es lo mismo
	MOVLW	0X00 ; al registro W un numero en hexadecimal
	MOVWF	PORTB	;a un file que es el puerto B F(File)
	GOTO 	INC ;incremente lo que se tiene en el puerto

INC
	ADDLW 	0x01 ;se lo suma
	MOVWF	PORTB	;lo mueve a puerto B
	GOTO	INC
END
;PIC se tiene que tener siempre un ciclo infinito
;PORT en el banco 0
;tris configuracion y el port administracion



