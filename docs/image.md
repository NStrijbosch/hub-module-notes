The Image class controls allows to make images to be displayed on the screen of the hub. It can be used via `hub.Image`

# Make an Image

## Image()

`Image()`

Define a custom image. 

__Parameters:__

*  [image](data_types.md#image) image_def: one of the following structures:

__Sample code:__

``` python
from hub import Image

# all values in range 0,1,...,9

imageN =    Image("90009:"
                  "99009:"
                  "90909:"
                  "90099:"
                  "90009")    

imageH = Image("70007\n70007\n66666\n70007\n70007")
```

## set_pixel()

`image.set_pixel(x,y,brightness)`

In the [image](data_types.md#image) set pixel (x,y) to given brightness

> Only works for custom images

__Parameters:__

*  x [int](data_types.md#int) x: in range [0,5]
*  y [int](data_types.md#int) y: in range [0,5]
*  brightness [int](data_types.md#int):  in range [0,10]

__Sample code:__

``` python
from hub import Image

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageH.set_pixel(2,2,0)
```

## shift_up()

`image.shift_up(shift)`

Shift all pixels of the [image](data_types.md#image) up with shift pixels

> Only works for custom images

__Parameters:__

*  shift [int](data_types.md#int): in range [0,5]

__Sample code:__

``` python
from hub import Image

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageH.shift_up(1)
```

## shift_down()

`image.shift_down(shift)`

Shift all pixels of the [image](data_types.md#image) down with shift pixels

> Only works for custom images

__Parameters:__

*  shift [int](data_types.md#int): in range [0,5]

__Sample code:__

``` python
from hub import Image

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageH.shift_down(1)
```

## shift_left()

`image.shift_left(shift)`

Shift all pixels of the [image](data_types.md#image) left with shift pixels

> Only works for custom images

__Parameters:__

*  shift [int](data_types.md#int): in range [0,5]

__Sample code:__

``` python
from hub import Image

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageH.shift_left(1)
```
## shift_right()

`image.shift_right(shift)`

Shift all pixels of the [image](data_types.md#image) right with shift pixels

> Only works for custom images

__Parameters:__

*  shift [int](data_types.md#int): in range [0,5]

__Sample code:__

``` python
from hub import Image

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageH.shift_right(1)
```
# Image info

## width()

`image.width()` 

Get width of [image](data_types.md#image).

__Returns:__

*  [integer](data_types.md#integer) width.

__Sample code:__

``` python
from hub import Image

imageH = Image("70007\n70007\n66666\n70007\n70007")
print("Width: " + str(imageH.width()))
```

```
>>> Width: 5
```
## Height()

`image.height()` 

Get height of [image](data_types.md#image).

__Returns:__

*  [integer](data_types.md#integer) height.

__Sample code:__

``` python
from hub import Image

imageH = Image("70007\n70007\n66666\n70007\n70007")
print("Height: " + str(imageH.height()))
```

```
>>> Height: 5
```

## get_pixel()

`image.get_pixel(x,y)` 

Get brightness of pixel (x,y).

__Parameters:__

*  x [int](data_types.md#int): x coordinate
*  y [int](data_types.md#int): y coordinate

__Returns:__

*  [int](data_types.md#int) brightness

__Sample code:__

``` python
from hub import Image

imageH = Image("70007\n70007\n66666\n70007\n70007")
print("Brightness pixel (2,2): " + str(imageH.get_pixel(2,2)))
```

```
>>> Brightness pixel (2,2): 6
```