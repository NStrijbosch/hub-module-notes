
<style type='text/css'>
.section ul { list-style: none !important; margin-left: 80px; margin-top:-3em;}
.section li { list-style: none !important}
.toctree-l2 a {margin-left: 0em;}
.toctree-l3 {margin-left: 2em;}
h2 {font-size: 125%;}
h2 {font-size: 115%;}
</style>

This class controls all functions linked to the buttons, i.e., the left, center, right, connect buttons on the hub.

```
hub.button.left 
hub.button.right
hub.button.center
hub.button.connect
```

## is_pressed()

```
hub.button.left.is_pressed()
```

Check if button is pressed 

__Returns:__

*  [boolean](data_types.md#bool) True if the button is pressed, otherwise False 


## was_pressed()

```
hub.button.left.was_pressed()
```
Check if button was pressed since last call

__Returns;__

*  [boolean](data_types.md#bool) True if the button was pressed since last call, otherwise False 

## pressed()
```
hub.button.right.pressed()
```

__Returns:__

* [integer](data_types.md#int) Number of presses since last call </br>


