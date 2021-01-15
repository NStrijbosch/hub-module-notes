
The display class controls all functions linked to the display. It can be used via `hub.display`. For more details see the examples below.


## show()

`hub.display.show(image)`

Show an image on the display.

__Parameters:__

*  [image](data_types.md#image) image. See [image](data_types.md#image) for all build in images and the [Image](image.md) class on how to create a custom image.

``` python
from hub import display

hub.display(hub.Image.HAPPY)
```

## clear()

```
display.clear()
```

Set the light intensity of all pixels to 0. 

__Sample code:__

``` python
from hub import display

hub.display(hub.Image.HAPPY)
hub.display.clear()
```

## pixel()

```
display.pixel(x, y, brightness)
```

__Parameters:__

*  x ([int](data_types.md#int)): x coordinate: value between 0 and 4
*  y ([int](data_types.md#int)): y coordinate: value between 0 and 4
*  brightness ([int](data_types.md#int)): brightness: value between 0 and 4

__Sample code:__

``` python
from hub import display

display.clear()
display.pixel(0,0,9)  #TODO check which corner
```

## rotate()

`display.rotate(angle)`

Change the orientation of the display. 

> Keep in mind this rotation is not reset at the start of each program. 

__Parameters:__

*  angle in degrees ([int](data_types.md#int): value of either 0, 90, 180, or 270

__Sample code:__

``` python
from hub import display

display.show(hub.Image.HAPPY)

display.rotate(90)
```

## align()

`hub.display.align(direction)`

Set the orientation of display.

> There does not seem a relation between direction and orientation

__Parameters:__

*  direction [int](data_types.md#int): value could be  
   1: default  
   2: 90 degrees clockwise with respect to default  
   4: 180 degrees with respect to default  
   5: 90 degrees counter clockwise with respect to default

> Difference between rotate() and align(): align() is absolute rotation, rotate() is relative rotation to current orientation of display. 

__Sample code:__

``` python
from hub import display

display.show(hub.Image.HAPPY)

display.align(4)
```

## invert()

`display.invert(invert)`

Invert the brightness of all pixels: 9 -> 0, 8 -> 1, ...

__Parameters:__

*  invert [bool](data_types.md#bool): `True`: invert led brightness; `False`: keep default brightness.

__Sample code:__

``` python
from hub import display

display.show(hub.Image.HAPPY)

display.invert(True)
```

## callback() TODO

unknown behaviour


