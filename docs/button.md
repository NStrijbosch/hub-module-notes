# Button

This class controls all functions linked to the buttons, i.e., the left, center, right, connect buttons on the hub.

```
hub.button.left 
hub.button.right
hub.button.center
hub.button.connect
```

### is_pressed()

```
hub.button.left.is_pressed()
```

Check if button is pressed 

#### Returns

True if the button is pressed, otherwise False </br>
*  __type__: boolean </br>
*  __values__: True or False


### was_pressed()

```
hub.button.left.was_pressed()
```
Check if button was pressed since last call

#### Returns

&emsp; True if the button was pressed since last call, otherwise False </br>
&emsp; __type__: boolean </br>
&emsp; __values__: True or False

### pressed()
```
hub.button.right.pressed()
```
#### Returns

&emsp; Number of presses since last call </br>
&emsp; __type__: integer </br>
&emsp; __values__: 0,1,...