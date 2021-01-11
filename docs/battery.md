## info()

Returns battery information

__Returns:__

*  json string including: temperature; charge_voltage; charge_current, charge_voltage_filtered, error_state, charger_state, battery_capacity_left

Example:

``` python
{'temperature': 23.9, 'charge_voltage': 8357, 'charge_current': 353, 'charge_voltage_filtered': 8352, 'error_state': [0], 'charger_state': 1, 'battery_capacity_left': 100}
```

## capacity_left()

Measure the capacity of the battery left

__Returns:__

*  integer values between 0 and 100, in increments of 20

## current()

Measure the current

__Returns:__

*  integer: unit unkown

## voltage()

Measure the voltage of the battery

__Returns:__

*  integer unit unkown
  
## temperature()

Measure the temperature of battery

__Returns:__

*  float unit Celcius
  
## charger_detect()

check if a charger is detected

__Returns:__

*  integer: 1 if charger detected, 0 if charger not detected (have to check without USB cable)