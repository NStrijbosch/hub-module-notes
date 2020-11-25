<style type='text/css'>
.section ul { list-style: none !important; margin-left: 80px; margin-top:-3em;}
.section li { list-style: none !important}
.toctree-l2 a {margin-left: 0em;}
.toctree-l3 {margin-left: 2em;}
h2 {font-size: 125%;}
h2 {font-size: 115%;}
</style>



# Display

## pixel()

```
hub.display.pixel(x,y,intensity)
```

Set the ligth intensity of a single pixel.

__Parameters:__

*  [integer](data_types.md#integer) x: in range [0,5]
*  [integer](data_types.md#integer) y: in range [0,5]
*  [integer](data_types.md#integer) intensity:  in range [0,10]




## Callback

```
image = hub.Image(image_def)
```

Define a custom image. 

__Parameters:__

*  [image](data_types.md#image) image_def: one of the following structures

### examples:

```
image = hub.Image("90009:"
                  "09090:"
                  "00900:"
                  "09090:"
                  "90009")    
```

```
image = hub.Image("90009\n09090\n00900\n09090\n90009"
```

```
image = hub.Image(2, 2, b'\x08\x08\x08\x08')
```

## set_pixel()

```
image.set_pixel(x,y,intensity) 
``` 

In the [image](data_types.md#image) set pixel (x,y) to given intensity

> Only works for custom images

__Parameters:__

*  [integer](data_types.md#integer) x: in range [0,5]
*  [integer](data_types.md#integer) y: in range [0,5]
*  [integer](data_types.md#integer) intensity:  in range [0,10]

## width()

```
image.width()
```

Get width of [image](data_types.md#image).

__Returns:__

*  [integer](data_types.md#integer) width.

## width()

```
image.height()
```

Get height of [image](data_types.md#image).

__Returns:__

*  [integer](data_types.md#integer) height.

## get_pixel()

```
image.get_pixel(x,y)
```

Get intensity of pixel (x,y) in [image](data_types.md#image).

__Returns:__

*  [integer](data_types.md#integer) itensity.