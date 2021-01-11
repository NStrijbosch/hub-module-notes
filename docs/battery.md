## info()

``` python
hub.battery.info()
```

Returns battery information

__Returns:__

*  json string including: temperature; charge_voltage; charge_current, charge_voltage_filtered, error_state, charger_state, battery_capacity_left

Example:

``` python
{'temperature': 23.9, 'charge_voltage': 8357, 'charge_current': 353, 'charge_voltage_filtered': 8352, 'error_state': [0], 'charger_state': 1, 'battery_capacity_left': 100}
```

## capacity_left()

``` python
hub.battery.capacity()
```

Measure the capacity of the battery left.

__Returns:__

*  integer values between 0 and 100, in increments of 20

## current()

``` python
hub.battery.current()
```

Measure the current from battery to hub.

__Returns:__

*  integer: unit unkown

## voltage()

``` python
hub.battery.voltage()
```

Measure the voltage of the battery.

__Returns:__

*  integer unit unkown
  
## temperature()

``` python
hub.battery.temperature()
```

Measure the temperature of battery.

__Returns:__

*  float unit Celcius
  
## charger_detect()

``` python
hub.battery.charger_detect()
```

Check if a charger is detected.

__Returns:__

*  integer: 1 if charger detected, 0 if charger not detected (have to check without USB cable)