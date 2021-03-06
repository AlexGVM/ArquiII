;CONFIGURACION INICIAL
    ORG 0X00
    GOTO START

START
    bcf STATUS,RP1
    movlw b'01000001'
    movwf ADCON0
    bsf STATUS,RP0 ;banco 1
    bcf STATUS,RP1
    clrf TRISA ;puertos de salida
    clrf TRISB
    clrf TRISC
    clrf TRISD
    clrf TRISE
    movlw b'00000111'
    movwf OPTION_REG ;TMR0 preescaler, 1:156
    movlw b'00001110' ;Puerto A/D
    movwf ADCON1
    bsf TRISA,0 ;RA0 linea de entrada para el ADC
    bcf STATUS,RP0 ;banco 0
    bcf STATUS,RP1
    clrf PORTC ;limpieza
loop
    btfss INTCON,T0IF
    goto loop ;Esperar que el timer0 desborde
    bcf INTCON,T0IF ;Limpiar el indicador de desborde
    bsf ADCON0,GO ;Empezar la conversion A/D
wait
    btfsc ADCON0,GO ;la conversion esta completa? (=0)
    goto wait ;si no esperar
    movf ADRESH,W ;Si W=ADRESH
    movwf PORTC ;resultado en PORTC
    goto loop ;ir a loop
END