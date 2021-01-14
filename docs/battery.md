
## info()

`battery.info()`

Retrieve information on the

__Returns:__

*  [json string ](data_types.md#json) including:  
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
>>> {'temperature': 23.9, 'charge_voltage': 8357, 'charge_current': 353, 'charge_voltage_filtered': 8352, 'error_state': [0], 'charger_state': 1, 'battery_capacity_left': 100}
```

## capacity()

`battery.capacity()`

Measure the capacity of the battery left.

__Returns:__

*  [int](data_types.md#int) value between 0 and 100, in increments of 20

``` python
from hub import battery

print("Capacity left: " + str(battery.capacity()))
```

``` python
>>> Capacity left: 80
```

## current()

`battery.current()`

Measure the current of the battery.

__Returns:__

*  [int](data_types.md#int) with unknown unit

``` python
from hub import battery

print("Current: " + str(battery.current()))
```

``` python
>>> Current: ????
```

## voltage()

`battery.voltage()`

Measure the voltage of the battery.

__Returns:__

*  [int](data_types.md#int) with unknown unit

``` python
from hub import battery

print("Voltage: " + str(battery.voltage()))
```

``` python
>>> Voltage: ????
```

## temperature()

`battery.temperature()`

Measure the temperature of the battery.

__Returns:__

*  temperature ([float](data_types.md#float)) in Celcius

``` python
from hub import battery

print("Temperature: " + str(battery.voltage()))
```

``` python
>>> Temperature: 25.4
```

## charger_detect()

`battery.charger_detect()`

Check if a charger is pluged into the hub.

__Returns:__

*  [bool](data_types.md#bool): 'True' if charger detected, 'False' if charger not detected.

``` python
from hub import battery

charging = battery.charger_detect()

if charging:
    print("hub is charging")
else:
    print("hub is not charging")
```

```
>>> hub is charging
```