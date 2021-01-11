# Make Image

## Image()

``` python
image = hub.Image(image_def)
```

Define a custom image. 

__Parameters:__

*  [image](data_types.md#image) image_def: one of the following structures

### examples:

``` python
image = hub.Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")    
```

``` python
image = hub.Image("90009\n09090\n00900\n09090\n90009"
```

``` python
image = hub.Image(2, 2, b'\x08\x08\x08\x08')
```

## set_pixel()

``` python
image.set_pixel(x,y,intensity) 
``` 

In the [image](data_types.md#image) set pixel (x,y) to given intensity

> Only works for custom images

__Parameters:__

*  [integer](data_types.md#integer) x: in range [0,5]
*  [integer](data_types.md#integer) y: in range [0,5]
*  [integer](data_types.md#integer) intensity:  in range [0,10]

## shift_up()

``` python
myimage.shift_up(int shift)
``` 

Shift all pixels of myimage up with (shift) pixels

> Only works for custom images

__Parameters:__

*  [integer](data_types.md#integer) shift: in range [0,5]

## shift_down()

``` python
myimage.shift_down(int shift)
``` 

Shift all pixels of myimage down with (shift) pixels

> Only works for custom images

__Parameters:__

*  [integer](data_types.md#integer) shift: in range [0,5]

## shift_left()

``` python
myimage.shift_left(int shift)
``` 

Shift all pixels of myimage left with (shift) pixels

> Only works for custom images

__Parameters:__

*  [integer](data_types.md#integer) shift: in range [0,5]

## shift_up()

``` python
myimage.shift_right(int shift)
``` 

Shift all pixels of myimage right with (shift) pixels

> Only works for custom images

__Parameters:__

*  [integer](data_types.md#integer) shift: in range [0,5]

# Image info

## width()

``` python
image.width()
```

Get width of [image](data_types.md#image).

__Returns:__

*  [integer](data_types.md#integer) width.

## height()

``` python
image.height()
```

Get height of [image](data_types.md#image).

__Returns:__

*  [integer](data_types.md#integer) height.

## get_pixel()

``` python
image.get_pixel(x,y)
```

Get intensity of pixel (x,y) in [image](data_types.md#image).

__Returns:__

*  [integer](data_types.md#integer) itensity.