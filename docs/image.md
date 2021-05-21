!!! info
     LEGO has published official docs on the hub-module: [https://lego.github.io/MINDSTORMS-Robot-Inventor-hub-API/](https://lego.github.io/MINDSTORMS-Robot-Inventor-hub-API/)


Using the Image class you can make images to be displayed on the screen of the hub. It can be used via `hub.Image`. See [display](display.md) for details on how to show images on the display.

# Make an Image

## Image()

`Image()`

Define a custom image. 

__Parameters:__

*  [image](data_types.md#image) image_def: one of the following structures:

__Sample code:__

``` python
from hub import Image, display
from utime import sleep_ms

# all values in range 0,1,...,9

imageN =    Image("90009:"
                "99009:"
                "90909:"
                "90099:"
                "90009")

display.show(imageN)
sleep_ms(1000)
 # or
imageH = Image("70007\n70007\n66666\n70007\n70007")

imageL = Image(2, 3, b'\x09\x00\x08\x00\x07\x07') # width = 2, height=3, brightness in bitarray corresponding to number of pixels
Image(2, 3, bytearray([9,0,8,0,7,7]))

display.show(imageL)

```

## set_pixel()

`image.set_pixel(x,y,brightness)`

In the [image](data_types.md#image) set pixel (x,y) to given brightness

!!! warning
        Only works for custom images
        
__Parameters:__

*  x [int](data_types.md#int) x: in range [0,5]
*  y [int](data_types.md#int) y: in range [0,5]
*  brightness [int](data_types.md#int):  in range [0,10]

__Sample code:__

``` python
from hub import Image, display

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageH.set_pixel(2,2,0)
display.show(imageH)
```

# Image operations

## shift_up()

`image.shift_up(shift)`

Shift all pixels of the [image](data_types.md#image) up with shift pixels

!!! warning
    Only works for custom images

__Parameters:__

*  shift [int](data_types.md#int): number of pixels

__Sample code:__

``` python
from hub import Image, display

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageHup = imageH.shift_up(1)
display.show(imageHup)
```

## shift_down()

`image.shift_down(shift)`

Shift all pixels of the [image](data_types.md#image) down with shift pixels

!!! warning
    Only works for custom images

__Parameters:__

*  shift [int](data_types.md#int): number of pixels

__Sample code:__

``` python
from hub import Image, display

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageHdown = imageH.shift_down(1)
display.show(imageHdown)
```

## shift_left()

`image.shift_left(shift)`

Shift all pixels of the [image](data_types.md#image) left with shift pixels

!!! warning
    Only works for custom images

__Parameters:__

*  shift [int](data_types.md#int): number of pixels

__Sample code:__

``` python
from hub import Image, display

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageHleft = imageH.shift_left(1)
display.show(imageHleft)
```
## shift_right()

`image.shift_right(shift)`

Shift all pixels of the [image](data_types.md#image) right with shift pixels

!!! warning
    Only works for custom images

__Parameters:__

*  shift [int](data_types.md#int): in range [0,5]

__Sample code:__

``` python
from hub import Image, display

imageH = Image("70007\n70007\n66666\n70007\n70007")
imageHright = imageH.shift_right(1)
display.show(imageHright)
```
# Image info

## width()

`image.width()` 

Get width of [image](data_types.md#image).

__Returns:__

*  [int](data_types.md#int) width.

__Sample code:__

``` python
from hub import Image

imageH = Image("700079\n700079\n666669\n700079\n700079\n999999")
print("Width: " + str(imageH.width()))
```

<span class='shell_output'>
\> Width: 6
</span>
## Height()

`image.height()` 

Get height of [image](data_types.md#image).

__Returns:__

*  [int](data_types.md#int) height.

__Sample code:__

``` python
from hub import Image

imageH = Image("700079\n700079\n666669\n700079\n700079\n999999")
print("Height: " + str(imageH.height()))
```

<span class='shell_output'>
\> Height: 6
</span>

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

<span class='shell_output'>
\> Brightness pixel (2,2): 6
</span>






