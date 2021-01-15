The button class controls all functions linked to the buttons, i.e., left, center, right, connect. It can be used via:

```
hub.button.left 
hub.button.right
hub.button.center
hub.button.connect
```
See the examples below for more details.

## is pressed()

`button.left.is_pressed()`

Check if button is pressed.

__Returns:__

*  [boolean](data_types.md#bool): `True` if the button is pressed, otherwise `False`. 

__Sample code:__

``` python
from hub import button

while not button.left.is_pressed():
    print('press left button')
```

```
>>> press left button
>>> press left button
>>> press left button  (after left button is pressed messages stop)
```

## was_pressed()

`button.left.was_pressed()`

Check if button was pressed since last call.

__Returns:__

*  [boolean](data_types.md#bool) `True` if the button was pressed since last call, otherwise `False`

__Sample code:__

``` python
from hub import button
from utime import sleep_ms

while not button.left.was_pressed():
    print('press left button')
    sleep_ms(1000)
```

```
>>> press left button
>>> press left button
>>> press left button  (after this button is pressed)
```

## pressed()

`button.left.pressed()`

__Returns:__

* [integer](data_types.md#int): Number of presses since last call

__Sample code:__

``` python
from hub import button
from utime import sleep_ms

for i in range(3):
    print('number of presses: '+ str(button.left.pressed()))
    sleep_ms(2000)
```

```
number of presses: 0
number of presses: 3
number of presses: 1
```

## on_change() TODO

`button.left.on_change(lambda function)`

__Parameters:__

*  Lambda function? on todo, tested with print('hallo') did not work as expected




