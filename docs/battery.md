
## info()

`battery.info()`

Retrieve information of the hub

__Returns:__

*  [dictionary](data_types.md#dictionary) including:  
temperature  
charge_voltage  
charge_current  
charge_voltage_filtered  
error_state  
charger_state  
battery_capacity_left  

__Sample code:__

``` python
from hub import battery

print(battery.info())
```

``` python
> {'temperature': 20.2, 'charge_voltage': 8389, 'charge_current': 332, 'charge_voltage_filtered': 8359, 'error_state': [0], 'charger_state': 1, 'battery_capacity_left': 100}
```

## capacity_left()

`battery.capacity_left()`

Measure the capacity left in the battery.

__Returns:__

*  [int](data_types.md#int) value between 0 and 100, in increments of 20

``` python
from hub import battery

print("Capacity left: " + str(battery.capacity_left()))
```

``` python
> Capacity left: 80
```

## current()

`battery.current()`

Measure the (charge?) current of the battery.

__Returns:__

*  [int](data_types.md#int) with unknown unit

``` python
from hub import battery

print("Current: " + str(battery.current()))
```

``` python
> Current: 75
```

## voltage()

`battery.voltage()`

Measure the charging voltage of the battery.

__Returns:__

*  [int](data_types.md#int) with unknown unit

__Sample code__

``` python
from hub import battery

print("Voltage: " + str(battery.voltage()))
```

``` python
> Voltage: 8391
```

## temperature()

`battery.temperature()`

Measure the temperature of the battery.

__Returns:__

*  Temperature ([float](data_types.md#float)) in Celcius

``` python
from hub import battery

print("Temperature: " + str(battery.temperature()))
```

``` python
> Temperature: 21.0
```

## charger_detect()

`battery.charger_detect()`

Check if a charger is plugged into the hub.

__Returns:__

*  [bool](data_types.md#bool): 'True' if charger detected, 'False' if charger not detected.

__Sample code:__

``` python
from hub import battery

charging = battery.charger_detect()

if charging:
    print("hub is charging")
else:
    print("hub is not charging")
```

<span class='shell_output'>
\> hub is charging
</span>