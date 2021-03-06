EESchema Schematic File Version 2  date pon 21 apr 2014 00:06:39 CEST
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:tempcon2x16
EELAYER 25  0
EELAYER END
$Descr A4 11700 8267
encoding utf-8
Sheet 1 1
Title "noname.sch"
Date "20 apr 2014"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L VCC #PWR01
U 1 1 5353FE31
P 7100 3300
F 0 "#PWR01" H 7100 3400 30  0001 C CNN
F 1 "VCC" H 7100 3400 30  0000 C CNN
	1    7100 3300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR02
U 1 1 5353FE2A
P 7100 2550
F 0 "#PWR02" H 7100 2550 30  0001 C CNN
F 1 "GND" H 7100 2480 30  0001 C CNN
	1    7100 2550
	1    0    0    -1  
$EndComp
$Comp
L cd4051-ver1 Um1
U 1 1 5353FE09
P 7800 2850
F 0 "Um1" H 7900 2850 60  0000 C CNN
F 1 "cd4051-ver1" H 7900 2650 60  0000 C CNN
	1    7800 2850
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR03
U 1 1 53515E17
P 10550 2600
F 0 "#PWR03" H 10550 2600 30  0001 C CNN
F 1 "GND" H 10550 2530 30  0001 C CNN
	1    10550 2600
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR04
U 1 1 535384B6
P 8500 2550
F 0 "#PWR04" H 8500 2550 30  0001 C CNN
F 1 "GND" H 8500 2480 30  0001 C CNN
	1    8500 2550
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR05
U 1 1 53538452
P 2650 3450
F 0 "#PWR05" H 2650 3550 30  0001 C CNN
F 1 "VCC" H 2650 3550 30  0000 C CNN
	1    2650 3450
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR06
U 1 1 5353842A
P 2450 4450
F 0 "#PWR06" H 2450 4450 30  0001 C CNN
F 1 "GND" H 2450 4380 30  0001 C CNN
	1    2450 4450
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR07
U 1 1 53538427
P 2450 4450
F 0 "#PWR07" H 2450 4450 30  0001 C CNN
F 1 "GND" H 2450 4380 30  0001 C CNN
	1    2450 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	10450 2800 10150 2800
Wire Wire Line
	10450 3200 10150 3200
Wire Wire Line
	10050 3300 9300 3300
Wire Wire Line
	8500 3250 9600 3250
Wire Wire Line
	9600 3250 9600 3500
Wire Wire Line
	8500 3450 8500 3500
Wire Wire Line
	8500 3500 9500 3500
Wire Wire Line
	9500 3500 9500 3100
Wire Wire Line
	8500 2850 9350 2850
Wire Wire Line
	9350 2850 9350 2500
Wire Wire Line
	8500 2950 9200 2950
Wire Wire Line
	9200 2950 9200 2100
Wire Wire Line
	10550 2900 10150 2900
Wire Wire Line
	10150 3600 10450 3600
Wire Wire Line
	10050 2900 9450 2900
Wire Wire Line
	9350 2500 10050 2500
Wire Wire Line
	9200 2100 10050 2100
Wire Wire Line
	10550 3500 10150 3500
Wire Wire Line
	10550 2700 10150 2700
Wire Wire Line
	10550 2300 10150 2300
Wire Wire Line
	7750 850  8950 850 
Wire Wire Line
	8950 850  8950 2350
Wire Wire Line
	8950 2350 8500 2350
Wire Wire Line
	1000 4450 2250 4450
Wire Wire Line
	2250 4450 2250 4850
Wire Wire Line
	2250 4850 2450 4850
Wire Wire Line
	2950 4850 2950 4350
Wire Wire Line
	2950 4350 3950 4350
Wire Wire Line
	3950 4350 3950 4750
Wire Wire Line
	3050 2950 3750 2950
Wire Wire Line
	3750 2950 3750 2800
Wire Wire Line
	3750 2800 3850 2800
Wire Wire Line
	3050 3150 3500 3150
Wire Wire Line
	3500 3150 3500 3650
Wire Wire Line
	3500 3650 3850 3650
Wire Wire Line
	5350 2750 5650 2750
Wire Wire Line
	5650 2750 5650 2300
Wire Wire Line
	5650 2300 6000 2300
Wire Wire Line
	5350 3750 7100 3750
Wire Wire Line
	7100 3750 7100 3450
Wire Wire Line
	9450 2900 9450 3150
Wire Wire Line
	9450 3150 8500 3150
Wire Wire Line
	5350 3550 5350 3100
Wire Wire Line
	5350 3100 4350 3100
Wire Wire Line
	4350 3100 4350 3650
Wire Wire Line
	5350 2550 5350 2100
Wire Wire Line
	5350 2100 4350 2100
Wire Wire Line
	4350 2100 4350 2800
Connection ~ 4350 2650
Wire Wire Line
	3050 2450 2050 2450
Wire Wire Line
	2050 2450 2050 3050
Wire Wire Line
	4650 4800 4500 4800
Wire Wire Line
	4500 4800 4500 4950
Wire Wire Line
	4500 4950 3950 4950
Wire Wire Line
	1550 3050 1250 3050
Wire Wire Line
	1250 3050 1250 3350
Wire Wire Line
	1250 3350 1000 3350
Wire Wire Line
	8500 2450 9000 2450
Wire Wire Line
	9000 2450 9000 700 
Wire Wire Line
	9000 700  7750 700 
Wire Wire Line
	7750 700  7750 750 
Wire Wire Line
	8500 2250 8850 2250
Wire Wire Line
	8850 2250 8850 1000
Wire Wire Line
	8850 1000 7750 1000
Wire Wire Line
	7750 1000 7750 950 
Wire Wire Line
	10550 2100 10150 2100
Wire Wire Line
	10550 2500 10150 2500
Wire Wire Line
	10550 3300 10150 3300
Wire Wire Line
	10550 2600 10150 2600
Wire Wire Line
	10050 2300 9300 2300
Wire Wire Line
	10050 2700 9400 2700
Wire Wire Line
	9500 3100 10050 3100
Wire Wire Line
	10550 3100 10150 3100
Wire Wire Line
	10150 2200 10450 2200
Wire Wire Line
	9300 2300 9300 2750
Wire Wire Line
	9300 2750 8500 2750
Wire Wire Line
	9400 2700 9400 3050
Wire Wire Line
	9400 3050 8500 3050
Wire Wire Line
	9300 3300 9300 3350
Wire Wire Line
	9300 3350 8500 3350
Wire Wire Line
	9600 3500 10050 3500
Wire Wire Line
	10450 3000 10150 3000
Wire Wire Line
	10450 2400 10150 2400
Wire Wire Line
	10450 3400 10150 3400
$Comp
L VCC #PWR08
U 1 1 535383BF
P 4950 3050
F 0 "#PWR08" H 4950 3150 30  0001 C CNN
F 1 "VCC" H 4950 3150 30  0000 C CNN
	1    4950 3050
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR09
U 1 1 5353839F
P 4950 2250
F 0 "#PWR09" H 4950 2250 30  0001 C CNN
F 1 "GND" H 4950 2180 30  0001 C CNN
	1    4950 2250
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR010
U 1 1 5352EDB0
P 6000 1800
F 0 "#PWR010" H 6000 1800 30  0001 C CNN
F 1 "GND" H 6000 1730 30  0001 C CNN
	1    6000 1800
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR011
U 1 1 5352EDA3
P 6000 2800
F 0 "#PWR011" H 6000 2900 30  0001 C CNN
F 1 "VCC" H 6000 2900 30  0000 C CNN
	1    6000 2800
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR012
U 1 1 5352AFB9
P 10450 2400
F 0 "#PWR012" H 10450 2400 30  0001 C CNN
F 1 "GND" H 10450 2330 30  0001 C CNN
	1    10450 2400
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR013
U 1 1 5352AFAD
P 10450 2800
F 0 "#PWR013" H 10450 2800 30  0001 C CNN
F 1 "GND" H 10450 2730 30  0001 C CNN
	1    10450 2800
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR014
U 1 1 5352AF7E
P 10450 3600
F 0 "#PWR014" H 10450 3600 30  0001 C CNN
F 1 "GND" H 10450 3530 30  0001 C CNN
	1    10450 3600
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR015
U 1 1 5352AF73
P 10450 3400
F 0 "#PWR015" H 10450 3400 30  0001 C CNN
F 1 "GND" H 10450 3330 30  0001 C CNN
	1    10450 3400
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR016
U 1 1 5352AF66
P 10450 3200
F 0 "#PWR016" H 10450 3200 30  0001 C CNN
F 1 "GND" H 10450 3130 30  0001 C CNN
	1    10450 3200
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR017
U 1 1 5352AF56
P 10450 3000
F 0 "#PWR017" H 10450 3000 30  0001 C CNN
F 1 "GND" H 10450 2930 30  0001 C CNN
	1    10450 3000
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR018
U 1 1 5352AF46
P 11050 2700
F 0 "#PWR018" H 11050 2800 30  0001 C CNN
F 1 "VCC" H 11050 2800 30  0000 C CNN
	1    11050 2700
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR019
U 1 1 5352AF39
P 10450 2200
F 0 "#PWR019" H 10450 2200 30  0001 C CNN
F 1 "GND" H 10450 2130 30  0001 C CNN
	1    10450 2200
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR020
U 1 1 5352AF05
P 11050 2100
F 0 "#PWR020" H 11050 2200 30  0001 C CNN
F 1 "VCC" H 11050 2200 30  0000 C CNN
	1    11050 2100
	1    0    0    -1  
$EndComp
$Comp
L TEMPCON2X16 ConTemp1
U 1 1 5352AC29
P 10050 2800
F 0 "ConTemp1" H 9700 3600 60  0000 C CNN
F 1 "TEMPCON2X16" H 10550 3650 60  0000 C CNN
	1    10050 2800
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR021
U 1 1 53519790
P 1000 2250
F 0 "#PWR021" H 1000 2250 30  0001 C CNN
F 1 "GND" H 1000 2180 30  0001 C CNN
	1    1000 2250
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR022
U 1 1 53519784
P 1000 2350
F 0 "#PWR022" H 1000 2350 30  0001 C CNN
F 1 "GND" H 1000 2280 30  0001 C CNN
	1    1000 2350
	0    -1   -1   0   
$EndComp
$Comp
L VCC #PWR023
U 1 1 53519775
P 1000 2450
F 0 "#PWR023" H 1000 2550 30  0001 C CNN
F 1 "VCC" H 1000 2550 30  0000 C CNN
	1    1000 2450
	0    1    1    0   
$EndComp
$Comp
L GND #PWR024
U 1 1 535196DB
P 1550 3450
F 0 "#PWR024" H 1550 3450 30  0001 C CNN
F 1 "GND" H 1550 3380 30  0001 C CNN
	1    1550 3450
	1    0    0    -1  
$EndComp
$Comp
L C C1
U 1 1 535196A6
P 1550 3250
F 0 "C1" H 1600 3350 50  0000 L CNN
F 1 "10 u" H 1600 3150 50  0000 L CNN
	1    1550 3250
	1    0    0    -1  
$EndComp
$Comp
L C C2
U 1 1 5351969D
P 2450 4650
F 0 "C2" H 2500 4750 50  0000 L CNN
F 1 "10 u" H 2500 4550 50  0000 L CNN
	1    2450 4650
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 53519618
P 2700 4850
F 0 "R3" V 2780 4850 50  0000 C CNN
F 1 "1k" V 2700 4850 50  0000 C CNN
	1    2700 4850
	0    -1   -1   0   
$EndComp
$Comp
L R R2
U 1 1 53519609
P 1800 3050
F 0 "R2" V 1880 3050 50  0000 C CNN
F 1 "1k" V 1800 3050 50  0000 C CNN
	1    1800 3050
	0    -1   -1   0   
$EndComp
$Comp
L GND #PWR025
U 1 1 535195DC
P 1000 4350
F 0 "#PWR025" H 1000 4350 30  0001 C CNN
F 1 "GND" H 1000 4280 30  0001 C CNN
	1    1000 4350
	0    -1   -1   0   
$EndComp
$Comp
L CONN_8 ArduinoDig1
U 1 1 535194E8
P 7400 1100
F 0 "ArduinoDig1" V 7350 1100 60  0000 C CNN
F 1 "CONN_8" V 7450 1100 60  0000 C CNN
	1    7400 1100
	-1   0    0    1   
$EndComp
$Comp
L CONN_8 ArduinoDig2
U 1 1 535194E0
P 650 4100
F 0 "ArduinoDig2" V 600 4100 60  0000 C CNN
F 1 "CONN_8" V 700 4100 60  0000 C CNN
	1    650  4100
	-1   0    0    1   
$EndComp
$Comp
L CONN_6 ArduinoAnalogIn1
U 1 1 535194CD
P 650 3100
F 0 "ArduinoAnalogIn1" V 600 3100 60  0000 C CNN
F 1 "CONN_6" V 700 3100 60  0000 C CNN
	1    650  3100
	-1   0    0    1   
$EndComp
$Comp
L CONN_6 ArduinoPower1
U 1 1 535194BF
P 650 2400
F 0 "ArduinoPower1" V 600 2400 60  0000 C CNN
F 1 "CONN_6" V 700 2400 60  0000 C CNN
	1    650  2400
	-1   0    0    1   
$EndComp
$Comp
L VCC #PWR026
U 1 1 53519469
P 3550 5250
F 0 "#PWR026" H 3550 5350 30  0001 C CNN
F 1 "VCC" H 3550 5350 30  0000 C CNN
	1    3550 5250
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR027
U 1 1 53519460
P 3550 4450
F 0 "#PWR027" H 3550 4450 30  0001 C CNN
F 1 "GND" H 3550 4380 30  0001 C CNN
	1    3550 4450
	-1   0    0    1   
$EndComp
$Comp
L VCC #PWR028
U 1 1 53519440
P 4650 5300
F 0 "#PWR028" H 4650 5400 30  0001 C CNN
F 1 "VCC" H 4650 5400 30  0000 C CNN
	1    4650 5300
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR029
U 1 1 5351943C
P 4650 4300
F 0 "#PWR029" H 4650 4300 30  0001 C CNN
F 1 "GND" H 4650 4230 30  0001 C CNN
	1    4650 4300
	-1   0    0    1   
$EndComp
$Comp
L LM324N U1
U 3 1 53519417
P 3450 4850
F 0 "U1" H 3500 5050 60  0000 C CNN
F 1 "LM324N" H 3600 4650 50  0000 C CNN
	3    3450 4850
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR030
U 1 1 535193E0
P 3050 3650
F 0 "#PWR030" H 3050 3650 30  0001 C CNN
F 1 "GND" H 3050 3580 30  0001 C CNN
	1    3050 3650
	1    0    0    -1  
$EndComp
$Comp
L R R4
U 1 1 535193A6
P 3050 2700
F 0 "R4" V 3130 2700 50  0000 C CNN
F 1 "43.2 k" V 3050 2700 50  0000 C CNN
	1    3050 2700
	1    0    0    -1  
$EndComp
$Comp
L R R6
U 1 1 53519395
P 4100 2800
F 0 "R6" V 4180 2800 50  0000 C CNN
F 1 "22k" V 4100 2800 50  0000 C CNN
	1    4100 2800
	0    -1   -1   0   
$EndComp
$Comp
L LM324N U1
U 1 1 535190F2
P 4850 3650
F 0 "U1" H 4900 3850 60  0000 C CNN
F 1 "LM324N" H 5000 3450 50  0000 C CNN
	1    4850 3650
	-1   0    0    1   
$EndComp
$Comp
L R R7
U 1 1 53519311
P 4100 3650
F 0 "R7" V 4180 3650 50  0000 C CNN
F 1 "22k" V 4100 3650 50  0000 C CNN
	1    4100 3650
	0    -1   -1   0   
$EndComp
$Comp
L R R5
U 1 1 535192FD
P 3050 3400
F 0 "R5" V 3130 3400 50  0000 C CNN
F 1 "43.2k" V 3050 3400 50  0000 C CNN
	1    3050 3400
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR031
U 1 1 535192E3
P 2650 2650
F 0 "#PWR031" H 2650 2650 30  0001 C CNN
F 1 "GND" H 2650 2580 30  0001 C CNN
	1    2650 2650
	-1   0    0    1   
$EndComp
$Comp
L LM324N U1
U 2 1 53519288
P 2550 3050
F 0 "U1" H 2600 3250 60  0000 C CNN
F 1 "LM324N" H 2700 2850 50  0000 C CNN
	2    2550 3050
	-1   0    0    1   
$EndComp
$Comp
L R R9
U 1 1 535191C0
P 6000 2550
F 0 "R9" V 6080 2550 50  0000 C CNN
F 1 "1k" V 6000 2550 50  0000 C CNN
	1    6000 2550
	1    0    0    -1  
$EndComp
$Comp
L VR VR2
U 1 1 535191A6
P 6000 2050
F 0 "VR2" V 6080 2050 50  0000 C CNN
F 1 "0.5 k max" V 6000 2050 50  0000 C CNN
	1    6000 2050
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR032
U 1 1 53519190
P 4950 4050
F 0 "#PWR032" H 4950 4150 30  0001 C CNN
F 1 "VCC" H 4950 4150 30  0000 C CNN
	1    4950 4050
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR033
U 1 1 5351915A
P 4950 3250
F 0 "#PWR033" H 4950 3250 30  0001 C CNN
F 1 "GND" H 4950 3180 30  0001 C CNN
	1    4950 3250
	-1   0    0    1   
$EndComp
$Comp
L LM324N U1
U 4 1 53519103
P 4850 2650
F 0 "U1" H 4900 2850 60  0000 C CNN
F 1 "LM324N" H 5000 2450 50  0000 C CNN
	4    4850 2650
	-1   0    0    1   
$EndComp
$Comp
L GND #PWR034
U 1 1 53518FED
P 7100 2350
F 0 "#PWR034" H 7100 2350 30  0001 C CNN
F 1 "GND" H 7100 2280 30  0001 C CNN
	1    7100 2350
	0    1    1    0   
$EndComp
$Comp
L VCC #PWR035
U 1 1 53518E8B
P 11050 2300
F 0 "#PWR035" H 11050 2400 30  0001 C CNN
F 1 "VCC" H 11050 2400 30  0000 C CNN
	1    11050 2300
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR036
U 1 1 53518E85
P 11050 3500
F 0 "#PWR036" H 11050 3600 30  0001 C CNN
F 1 "VCC" H 11050 3600 30  0000 C CNN
	1    11050 3500
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR037
U 1 1 53518E80
P 11050 3300
F 0 "#PWR037" H 11050 3400 30  0001 C CNN
F 1 "VCC" H 11050 3400 30  0000 C CNN
	1    11050 3300
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR038
U 1 1 53518E7C
P 11050 3100
F 0 "#PWR038" H 11050 3200 30  0001 C CNN
F 1 "VCC" H 11050 3200 30  0000 C CNN
	1    11050 3100
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR039
U 1 1 53518E77
P 11050 2900
F 0 "#PWR039" H 11050 3000 30  0001 C CNN
F 1 "VCC" H 11050 3000 30  0000 C CNN
	1    11050 2900
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR040
U 1 1 53518E6C
P 11050 2500
F 0 "#PWR040" H 11050 2600 30  0001 C CNN
F 1 "VCC" H 11050 2600 30  0000 C CNN
	1    11050 2500
	1    0    0    -1  
$EndComp
$Comp
L VCC #PWR041
U 1 1 53518E62
P 2850 1350
F 0 "#PWR041" H 2850 1450 30  0001 C CNN
F 1 "VCC" H 2850 1450 30  0000 C CNN
	1    2850 1350
	1    0    0    -1  
$EndComp
$Comp
L R R1-8
U 1 1 53515BEB
P 10800 3500
F 0 "R1-8" V 10880 3500 50  0000 C CNN
F 1 "1k" V 10800 3500 50  0000 C CNN
	1    10800 3500
	0    -1   -1   0   
$EndComp
$Comp
L R R1-7
U 1 1 53515BDA
P 10800 3300
F 0 "R1-7" V 10880 3300 50  0000 C CNN
F 1 "1k" V 10800 3300 50  0000 C CNN
	1    10800 3300
	0    -1   -1   0   
$EndComp
$Comp
L R R1-6
U 1 1 53515BD1
P 10800 3100
F 0 "R1-6" V 10880 3100 50  0000 C CNN
F 1 "1k" V 10800 3100 50  0000 C CNN
	1    10800 3100
	0    -1   -1   0   
$EndComp
$Comp
L R R1-5
U 1 1 53515BC1
P 10800 2900
F 0 "R1-5" V 10880 2900 50  0000 C CNN
F 1 "1k" V 10800 2900 50  0000 C CNN
	1    10800 2900
	0    -1   -1   0   
$EndComp
$Comp
L R R1-4
U 1 1 53515BBA
P 10800 2700
F 0 "R1-4" V 10880 2700 50  0000 C CNN
F 1 "1k" V 10800 2700 50  0000 C CNN
	1    10800 2700
	0    -1   -1   0   
$EndComp
$Comp
L R R1-3
U 1 1 53515BAE
P 10800 2500
F 0 "R1-3" V 10880 2500 50  0000 C CNN
F 1 "1k" V 10800 2500 50  0000 C CNN
	1    10800 2500
	0    -1   -1   0   
$EndComp
$Comp
L R R1-2
U 1 1 53515B9D
P 10800 2300
F 0 "R1-2" V 10880 2300 50  0000 C CNN
F 1 "1k" V 10800 2300 50  0000 C CNN
	1    10800 2300
	0    -1   -1   0   
$EndComp
$Comp
L VR VR1
U 1 1 53515704
P 4650 4550
F 0 "VR1" V 4730 4550 50  0000 C CNN
F 1 "0.5 k max" V 4650 4550 50  0000 C CNN
	1    4650 4550
	1    0    0    -1  
$EndComp
$Comp
L R R8
U 1 1 535156C1
P 4650 5050
F 0 "R8" V 4730 5050 50  0000 C CNN
F 1 "R" V 4650 5050 50  0000 C CNN
	1    4650 5050
	1    0    0    -1  
$EndComp
$Comp
L R R1-1
U 1 1 535156B5
P 10800 2100
F 0 "R1-1" V 10880 2100 50  0000 C CNN
F 1 "1k" V 10800 2100 50  0000 C CNN
	1    10800 2100
	0    -1   -1   0   
$EndComp
$EndSCHEMATC
