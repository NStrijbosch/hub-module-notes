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

build in images
```
hub.Image.ALL_ARROWS
hub.Image.ALL_CLOCKS      
hub.Image.ANGRY           
hub.Image.ARROW_E         
hub.Image.ARROW_N
hub.Image.ARROW_NE        
hub.Image.ARROW_NW        
hub.Image.ARROW_S         
hub.Image.ARROW_SE
hub.Image.ARROW_SW        
hub.Image.ARROW_W         
hub.Image.ASLEEP          
hub.Image.BUTTERFLY
hub.Image.CHESSBOARD      
hub.Image.CLOCK1          
hub.Image.CLOCK10         
hub.Image.CLOCK11
hub.Image.CLOCK12         
hub.Image.CLOCK2          
hub.Image.CLOCK3          
hub.Image.CLOCK4
hub.Image.CLOCK5          
hub.Image.CLOCK6          
hub.Image.CLOCK7          
hub.Image.CLOCK8
hub.Image.CLOCK9          
hub.Image.CONFUSED        
hub.Image.COW             
hub.Image.DIAMOND
hub.Image.DIAMOND_SMALL   
hub.Image.DUCK            
hub.Image.FABULOUS        
hub.Image.GHOST
hub.Image.GIRAFFE         
hub.Image.GO_DOWN         
hub.Image.GO_LEFT         
hub.Image.GO_RIGHT
hub.Image.GO_UP           
hub.Image.HAPPY           
hub.Image.HEART           
hub.Image.HEART_SMALL
hub.Image.HOUSE           
hub.Image.MEH             
hub.Image.MUSIC_CROTCHET  
hub.Image.MUSIC_QUAVER
hub.Image.MUSIC_QUAVERS   
hub.Image.NO              
hub.Image.PACMAN          
hub.Image.PITCHFORK
hub.Image.RABBIT          
hub.Image.ROLLERSKATE     
hub.Image.SAD             
hub.Image.SILLY
hub.Image.SKULL           
hub.Image.SMILE           
hub.Image.SNAKE           
hub.Image.SQUARE
hub.Image.SQUARE_SMALL    
hub.Image.STICKFIGURE     
hub.Image.SURPRISED       
hub.Image.SWORD
hub.Image.TARGET          
hub.Image.TORTOISE        
hub.Image.TRIANGLE        
hub.Image.TRIANGLE_LEFT
hub.Image.TSHIRT          
hub.Image.UMBRELLA        
hub.Image.XMAS            
hub.Image.YES
```

## Sound

Waveforms

``` 
hub.sound.SOUND_SIN=0       
hub.sound.SOUND_SQUARE=1
hub.sound.SOUND_TRIANGLE=2
hub.sound.SOUND_SAWTOOTH=3
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

# Constants

```
hub.port.A.motor.BUSY_MODE = 0
hub.port.A.motor.BUSY_MOTOR = 1
```


```
hub.port.A.motor.EVENT_COMPLETED = 0
hub.port.A.motor.EVENT_INTERRUPTED = 1
```

```
hub.port.A.motor.FORMAT_RAW = 0
hub.port.A.motor.FORMAT_PCT = 1
hub.port.A.motor.FORMAT_SI = 2
```

```
hub.port.A.motor.PID_POSITION = 0
hub.port.A.motor.PID_SPEED = 1
```


```
hub.port.A.motor.STOP_FLOAT = 0
hub.port.A.motor.STOP_BRAKE = 1
hub.port.A.motor.STOP_HOLD = 2
```


## Sensors

