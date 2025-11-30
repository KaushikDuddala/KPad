# KPad v1!

The KPad is a simple macropad made by me just to learn the process and hopefully make revisions or a full keyboard in the future!! This was made using KMK, KiCad, Fusion 360, and more. 

## Features:

 - 128x32 OLED with volume display
 - EC11 Encoder for Volume
 - 16 SK6812 LEDs for underglow!!
 - 8 keys + physical key in the ec11
 - KMK firmware

 ## Future Features:
 - Swappable Modes (Single key swaps a mode that chaanges all key functions)
 - VIA support
 - Better software LED control
 - Better case design
 - Acrylic rather than hole in case

## Final Design

![Full Design](https://github.com/KaushikDuddala/KPad/blob/main/images/fullDesign.png?raw=true)


## PCB Design:


![Schematic](https://github.com/KaushikDuddala/KPad/blob/main/images/schematic.png?raw=true)
![PCB Design](https://github.com/KaushikDuddala/KPad/blob/main/images/PCBDesign.png?raw=true)
![PCB 3D Model](https://github.com/KaushikDuddala/KPad/blob/main/images/3DPCB.png?raw=true)

## Case:

![Bottom Half P1](https://github.com/KaushikDuddala/KPad/blob/main/images/caseBottom1.png?raw=true)
![Bottom Half P2](https://github.com/KaushikDuddala/KPad/blob/main/images/caseBottom2.png?raw=true)
![Top Half P1](https://github.com/KaushikDuddala/KPad/blob/main/images/caseTop1.png?raw=true)
![Top Half P2](https://github.com/KaushikDuddala/KPad/blob/main/images/caseTop2.png?raw=true)

## Bill of Materials (BOM):


- x9 1N4148 Diodes
- x8 Cherry MX switches
- x8 Keycaps
- x1 EC11 Encoder w/ switch
- x1 128x32 0.91" OLED screen
- x1 Seeed Studio XIAO RP2040
- x16 SK6812 LEDs
- x1 Case (2 3d printed halves)
- x4 M3x16mm Screws
- x4 M3x5mmx4mm heatset inserts


|Id |Designator                                            |Footprint                                     |Quantity|Designation         |
|---|------------------------------------------------------|----------------------------------------------|--------|--------------------|
|1  |D22,D17,D18,D24,D19,D20,D23,D25,D21                   |D_DO-35_SOD27_P7.62mm_Horizontal              |9       |1N4148              |
|2  |SW3,SW9,SW4,SW6,SW8,SW5,SW7,SW2                       |SW_Cherry_MX_1.00u_PCB                        |8       |SW_Push             |
|3  |SW1                                                   |RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm|1       |RotaryEncoder_Switch|
|4  |J1                                                    |SSD1306-0.91-OLED-4pin-128x32                 |1       |Conn_01x04          |
|5  |U1                                                    |XIAO-RP2040-DIP                               |1       |XIAO-RP2040-DIP     |
|6  |D9,D4,D15,D7,D12,D2,D14,D3,D13,D8,D6,D11,D10,D1,D5,D16|LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm        |16      |SK6812MINI          |


