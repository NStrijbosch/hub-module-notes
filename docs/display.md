
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

## show()

```
hub.display.show(image)
```

Show image on screen

__Parameters:__

*  [image](data_types.md#image) image

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


