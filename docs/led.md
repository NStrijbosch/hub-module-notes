
The Led class controls all functions linked to the led ring around the center button on the hub.

## led(color)

`hub.led(color)`

Turn on the led with a given [ledcolor](data_types.md#led)

__Parameter:__

*  [ledcolor](data_types.md#led):  
   0: Off  
   1:  Pink           
   2:  Violet             
   3:  Blue           
   4:  Light blue     
   5:  Light green    
   6:  Green          
   7:  Yellow         
   8:  Orange         
   9:  Red             
   10: Bright white   
   11: white          

__Sample code:__

``` python
import hub

hub.led(7)  # set led light to yellow
```

## led(r,g,b)

`hub.led(r,g,b)`

Turn the led color to a color defined by RGB values

__Parameters:__  

*  r [int](data_types.md#int) red value between 0 and 255
*  g [int](data_types.md#int) green value between 0 and 255
*  b [int](data_types.md#int) blue value between 0 and 255

!!! info
      keep in mind that the colors seem skewed towards blue


__Returns:__

* tuple (int r,int g,int b) each has a value between 0 and 255. Only if no arguments are given.

__Sample code:__
``` python
import hub

hub.led(0,100,50)
```


 

