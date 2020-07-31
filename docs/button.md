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
&emsp; __type__: boolean </br>
&emsp; __values__: True or False


### was_pressed()

```
hub.button.left.was_pressed()
```
Check if button was pressed since last call

#### Returns

True if the button was pressed since last call, otherwise False </br>
&emsp; __type__: boolean </br>
&emsp; __values__: True or False

### pressed()
```
hub.button.right.pressed()
```
#### Returns

Number of presses since last call </br>
&emsp; __type__: integer </br>
&emsp; __values__: 0,1,...


<style type='text/css'>
.class {
   border: 1px dashed #FF0000;
   color: #ffffff;
   text-align: center;
   width: 100px;
   margin: 0px;
   padding: 4px;
   }
</style>


<div class="class">
Class CSS  
[gesture](data_types.md#gesture) 
</div>