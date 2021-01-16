


# Hub status

## info()

`hub.info()`

Get hub information.

__Returns:__

* [dictionary](data_types.md#dictionary) including:  
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

<span class='shell_output'>
\> {'usb_vid': 1684, 'device_uuid': '03970000-3900-5000-1851-383332353732', '1ms_tick_on_time': 99.8596, 'usb_pid': 9, '1ms_tick_min': 58000.0, '1ms_tick_miss': 1022, 'hardware_version': 'Version_E', '1ms_tick_max': 2.6265e+07, 'product_variant': 0, '1ms_tick_total': 728280}
</span>


## status()

`hub.status()`

Get hub status of hub including all sensors and motors

__Returns:__ 

*  [dictionary](data_types.md#dictionary) including:  
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
>>> {'gyroscope': (0, 0, 0), 'port': {'C': [], 'D': [], 'B': [], 'E': [], 'A': [0, 0, -2, 0], 'F': []}, 'accelerometer': (-78, -305, 966), 'yaw_pitch_roll': (-27, -17, 4), 'position': (-27, -17, 4), 'display': '00000:00000:00000:00000:00000'}
```

## temperature()

`hub.temperature()`

Get temperature of the hub (probably internal sensor?)

__Returns:__

* [float](data_types.md#float): Temperature of the hub in Celcius.

__Sample code:__

``` python
import hub

print('Temperature: ' + str(hub.temperature()))
```

```
>>> Temperature: 24.0
```

# Hub actions

## powerdown_timeout()

`hub.powerdown_timeout(time)`

Set the idle time until automatic power down.

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

## power_off() TODO

`power_off()`

> Not actual shutdown, display is cleared and led is turned off. Hub stays connected. 

__Sample code:__
``` python
import hub

hub.power_off()
```

## repl_restart() TODO

`repl_restart()`

Restart REPL, in running REPL nothing is observed, in SPIKE app: keyboard interrupt + error message. Not advised to use!


## file_tansfer() TODO

`file_transfer()`

Usage unknown