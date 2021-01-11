
This class controls all functions linked to the led ring around the center button on the hub.

## led()

```
hub.led(color)
```
Turn on the led with a given [___led-color___](data_types.md#led-color)

__Parameter:__

*  [___led-color___](data_types.md#led-color)


``` 
hub.led(r,g,b)
```

Turn the led color to a color defined by RGB values

__Parameters:__  

*  ___r___ (integer) red value between 0 and 255
*  ___g___ (integer) green value between 0 and 255
*  ___b___ (integer) blue value between 0 and 255

> keep in mind that the colors seem skewed towards blue

``` python
hub.led()

```

__Returns:__

* tuple (int r,int g,int b) each has a value between 0 and 255S


 

