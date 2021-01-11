## file_tansfer()

Unknown

## info()

Returns hub information

__Returns:__

* Json string including: usb_vid(?), device_uuid, 1ms_tick_on_time(?), usb_pid(?), 1ms_tick_min(?), 1ms_tick_miss(?), hardware_version, product_variant, 1ms_tick_total(?)

Example

``` python
{'usb_vid': 1684, 'device_uuid': '03970000-3900-5000-1851-383332353732', '1ms_tick_on_time': 99.9855, 'usb_pid': 9, '1ms_tick_min': 114000.0, '1ms_tick_miss': 82, 'hardware_version': 'Version_E', '1ms_tick_max': 3.6746e+07, 'product_variant': 0, '1ms_tick_total': 567713}

```

## power_off()

Expeted behaviour: power_off hub

Observed behaviour in REPL: led turns off hub stays connected

## powerdown_timeout()

Set the idle time until automatic power down

``` python
hub.powerdown_timeout(integer)

```

__Parameter:__ 

* integer: ms idle before powerdown (default 300000)

``` python
hub.powerdown_timeout()

```
Read current powerdown time

__Returns:__

* integer: ms ide before powerdown (default 300000)

## repl_restart()

Restart REPL, in running REPL nothing is observed

## reset()

Reboot the hub

## status()

Returns status of hub including all sensors

__Returns:__ 

*  Json string including: gyroscope,port, accelerometer, yaw_pitch_roll, position, display

``` python
{'gyroscope': (0, 0, 0), 'port': {'C': [], 'D': [], 'B': [], 'E': [], 'A': [], 'F': []}, 'accelerometer': (48, -89, 1010), 'yaw_pitch_roll': (-1, -5, -2), 'position': (-1, -5, -2), 'display': '09090:99999:99999:09990:00900'}
```

## temperature()

Returns temperature of hub (?)

__Returns:__

* float