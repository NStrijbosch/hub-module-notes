

## show()

```
hub.display.show(image)
```

Show image on screen

__Parameters:__

*  [image](data_types.md#image) image

## pixel()

```
hub.display.pixel(int x, int y, int b)
```

__Parameters:__

*  int x: x coordinate value between 0 and 4
*  int y: y coordinate value between 0 and 4
*  int b: brightness value between 0 and 9

## clear()

```
hub.display.clear()
```

set the light intensity of all pixels to 0. 

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


