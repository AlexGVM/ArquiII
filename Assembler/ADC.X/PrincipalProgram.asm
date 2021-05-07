; PIC16F877A Configuration Bit Settings

; Assembly source line config statements

#include "p16f877a.inc"

; CONFIG

; __config 0xFF32
 __CONFIG _FOSC_HS & _WDTE_OFF & _PWRTE_ON & _BOREN_OFF & _LVP_OFF & _CPD_OFF & _WRT_OFF & _CP_OFF

	ORG	    0
	GOTO    INICIO
INICIO
	BSF	STATUS,RP0
	CLRF    TRISD ;SALIDA
	BSF	TRISA,0; RA0 ENTRADA ; se asigna RA0 como entrada
	CLRF	TRISC; SALIDA ; salida para todo el puerto C
	BSF	ADCON1,3 ;1
	BSF	ADCON1,2 ;1
	BSF	ADCON1,1 ;1
	BCF	ADCON1,0 ;0 1110-> RAO AN0 = ANALOGO
	BSF	ADCON1,6 ;FRECUENCIA OSCILADOR
	BCF	ADCON1,7 ;JUSTIFICACION IZQ
	BCF	STATUS,RP0
	BSF	ADCON0,7
	BCF	ADCON0,6 ; clock/64 
	BCF	ADCON0,5 ;0
	BCF	ADCON0,4 ;0
	BCF	ADCON0,3 ;CANAL AN0 = 000
	BSF	ADCON0,0 ;ADC ON
START
	BSF	ADCON0,2;GO/DONE -> 1
ADC	BTFSC	ADCON0,2 ;0 = va saltar
	GOTO	ADC
	MOVF	ADRESH,W
	MOVWF	PORTD
	GOTO	START
include "Delay.inc"
	END