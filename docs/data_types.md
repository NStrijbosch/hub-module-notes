# Data types

## int

## str

## float

## bool

## bytearray

## tuple

## list

# Constants

## hub

'''
hub.TOP = 0
hub.FRONT = 1
hub.RIGHT = 2
hub.BOTTOM = 3
hub.BACK = 4
hub.LEFT = 5
'''
## Battery

``` python
hub.battery.BATTERY_VOLTAGE_TOO_LOW=-5  
hub.battery.BATTERY_BAD_BATTERY=-4
hub.battery.BATTERY_TEMPERATURE_SENSOR_FAIL=-3
hub.battery.BATTERY_TEMPERATURE_OUT_OF_RANGE=-2
hub.battery.BATTERY_HUB_TEMPERATURE_CRITICAL_OUT_OF_RANGE=-2
hub.battery.BATTERY_NO_ERROR=0
```

``` python
hub.battery.CHARGER_STATE_FAIL=-1  
hub.battery.CHARGER_STATE_DISCHARGING=0
hub.battery.CHARGER_STATE_CHARGING_ONGOING=1  
hub.battery.CHARGER_STATE_CHARGING_COMPLETED=2
```

``` python
hub.battery.USB_CH_PORT_NONE=0
hub.battery.USB_CH_PORT_SDP=1
hub.battery.USB_CH_PORT_CDP=2
hub.battery.USB_CH_PORT_DCP=3                 
```

## Button

## Display

## Image

## Led

## Motion

### gesture

Orientation or movement of the hub measured with build in gyroscope and accelerometer

possible gestures:

```
hub.motion.BACK
hub.motion.DOUBLETAPPED
hub.motion.DOWN
hub.motion.FREEFALL
hub.motion.FRONT
hub.motion.LEFTSIDE
hub.motion.NONE
hub.motion.RIGHTSIDE
hub.motion.SHAKE
hub.motion.TAPPED
hub.motion.UP
```

## Motors

## Sensors

### Color

possible colors:
