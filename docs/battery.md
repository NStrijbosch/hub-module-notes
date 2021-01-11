## capacity_left()

__Returns:__

*  integer

## charger_detect()

__Returns:__

*  integer 0 or 1?

## current()

__Returns:__

*  integer
  
## info()

__Returns:__

*  json string including: temperature; charge_voltage; charge_current, charge_voltage_filtered, error_state, charger_state, battery_capacity_left

Example:

```
{'temperature': 23.9, 'charge_voltage': 8357, 'charge_current': 353, 'charge_voltage_filtered': 8352, 'error_state': [0], 'charger_state': 1, 'battery_capacity_left': 100}
```
  
## temperature()

__Returns:__

*  float

## voltage()

__Returns:__

*  integer