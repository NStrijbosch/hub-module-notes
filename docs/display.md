
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

```
hub.display.rotate(angle)
```

Change orientation of of display. 

> Keep in mind this rotation is not reset at the start of each program. 

__Parameters:__

*  [integer](data_types.md#integer) angle: 0, 90, 180, 270

## align()

``` python
hub.display.align()
```
Set orientation of display.

__Parameters:__

*  integer: (1: default, 2: 90 degrees clockwise with respect to default, 4: 180 degrees with respect to default, 5: 90 degrees counter clockwise with respect to default)

> Difference rotate() and align(): align is absolute rotation, rotate is relative rotation to current orientation of display.

## invert()

``` python
hub.display.invert(bool)
```

__Parameters:__

* bool: True: invert led brightness; False: keep default brightness

## callback()

unknown behaviour


