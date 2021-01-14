# Hub status

## info()

`hub.info()`

Get all hub information.

__Returns:__

* [json string](data_types.md#json) including:  
  usb_vid(?)  
  device_uuid  
  1ms_tick_on_time(?)  
  usb_pid(?)  
  1ms_tick_min(?)  
  1ms_tick_miss(?)  
  hardware_version  
  product_variant  
  1ms_tick_total(?)

__Sample code:__

``` python
import hub

print(hub.info())
```

```
>>> {'usb_vid': 1684, 'device_uuid': '03970000-3900-5000-1851-383332353732', '1ms_tick_on_time': 99.9855, 'usb_pid': 9, '1ms_tick_min': 114000.0, '1ms_tick_miss': 82, 'hardware_version': 'Version_E', '1ms_tick_max': 3.6746e+07, 'product_variant': 0, '1ms_tick_total': 567713}
```

## status()

`hub.status()`

Get hub status of hub including all sensors and motors

__Returns:__ 

*  [json string](data_types.md#json) including:  
   gyroscope
   port
   accelerometer
   yaw_pitch_roll
   position
   display

``` python
import hub

print(hub.status())
```

```
>>> {'gyroscope': (0, 0, 0), 'port': {'C': [], 'D': [], 'B': [], 'E': [], 'A': [], 'F': []}, 'accelerometer': (48, -89, 1010), 'yaw_pitch_roll': (-1, -5, -2), 'position': (-1, -5, -2), 'display': '09090:99999:99999:09990:00900'}
```

## temperature()

`hub.temperature()`

Get temperature of the hub (?)

__Returns:__

* [float](data_types.md#float) Temperature of the hub in Celcius.

# Hub actions

## powerdown_timeout()

`hub.powerdown_timeout(time)`

Set the idle time until automatic power down

__Parameters:__

*  time ([int](data_types.md#int)) in milliseconds.

__Returns:__

*  current idle time untill automatic power down (default is 30000). Only if no argument is provided. 

__Sample code:__

``` python
import hub

hub.powerdown_timeout(40000)

print('Time until automatic powerdown: '+str(hub.powerdown_timeout())+ ' ms')
```
```
>>> Time until automatic powerdown: 40000 ms
``` 

## reset()

`hub.reset()`

Roboot the hub.

__Sample code:__

``` python
import hub

hub.reset()
```

# TODO

## repl_restart()

Restart REPL, in running REPL nothing is observed

## power_off()

Expeted behaviour: power_off hub

Observed behaviour in REPL: led turns off hub stays connected


## file_tansfer()

Unknown