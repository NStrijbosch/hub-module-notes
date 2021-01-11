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

``` python
hub.TOP = 0
hub.FRONT = 1
hub.RIGHT = 2
hub.BOTTOM = 3
hub.BACK = 4
hub.LEFT = 5
```

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

## Image

## Sound

Waveforms

``` 
hub.sound.SOUND_SIN       
hub.sound.SOUND_SQUARE
hub.sound.SOUND_TRIANGLE
hub.sound.SOUND_SAWTOOTH 
```

## Led

### led color:

|Number |Name                 |R   |G   |B  |
|-------|---------------------|----|----|---|
|0      |Off                  |0   |0   |0  |
|1      |Pink                 |255 |7   |20 |
|2      |Violet               |255 |10  |100|    
|3      |Blue                 |0   |0   |80 |
|4      |Light blue           |0   |57  |57 |
|5      |Light green          |0   |112 |28 |
|6      |Green                |0   |80  |0  |
|7      |Yellow               |255 |35  |0  |
|8      |Orange               |255 |15  |0  |
|9      |Red                  |255 |0   |0  |  
|10     |Bright white         |255 |70  |35 |
|11     |White                |102 |28  |14 |


## Motion

### gesture

movement of the hub measured with build in gyroscope and accelerometer

possible gestures:

```
hub.motion.TAPPED=0
hub.motion.DOUBLETAPPED=1
hub.motion.SHAKE=2
hub.motion.FREEFALL=3
```

## Port

###

attached port

```
hub.port.ATTACED = 1
hub.port.DETACHED = 0
```

Possible modes for a PU port

```
hub.port.MODE_DEFAULT = 0
hub.port.MODE_FULL_DUPLEX = 1
hub.port.MODE_HALF_DUPLEX = 2
hub.port.MODE_GPIO = 3
```


## Motors

## Sensors

