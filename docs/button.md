The button class controls all functions linked to the buttons, i.e., left, center, right, connect. It can be used via:

<span class='shell_output'>
hub.button.left </br>
hub.button.right  </br>
hub.button.center  </br>
hub.button.connect  
</span>

See the examples below for more details.

## is pressed()

`button.left.is_pressed()`

Check if button is pressed.

__Returns:__

*  [bool](data_types.md#bool): `True` if the button is pressed, otherwise `False`. 

__Sample code:__

``` python
from hub import button

while not button.left.is_pressed():
    print('press left button')
```

<span class='shell_output'>
\> press left button </br>
\> press left button</br>
\> press left button  (after left button is pressed messages stop)
</span>

## was_pressed()

`button.left.was_pressed()`

Check if button was pressed since last call.

__Returns:__

*  [bool](data_types.md#bool) `True` if the button was pressed since last call, otherwise `False`

__Sample code:__

``` python
from hub import button
from utime import sleep_ms

button.left.was_pressed() # first call; behaviour before program is unknown

while not button.left.was_pressed():
    print('press left button')
    sleep_ms(1000)
```

<span class='shell_output'>
\> press left button  
\> press left button  
\> press left button  (after this left button is pressed)  
</span>

## presses()

`button.left.presses()`

__Returns:__

* [integer](data_types.md#int): Number of presses since last call

__Sample code:__

``` python
from hub import button
from utime import sleep_ms

for i in range(4):
    print('number of presses: '+ str(button.left.presses()))
    sleep_ms(2000)
```

<span class='shell_output'>
\> number of presses: 0 </br>
\> number of presses: 3 </br>
\> number of presses: 1 </br> 
</span>

## on_change() TODO

`button.left.on_change(lambda function)`

!!! todo
    Not suffiently tested. What is parameter: Lambda function?, tested with print('hallo') did not work as expected




