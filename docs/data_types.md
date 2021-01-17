# Data types

The following data types are used.

## int

__int:__ 

*  Postive or negative whole number, e..g, `1`, `99`

## float

__float:__

*  any real number with a fractional component, e..g, `1.4`, `3.14`

## str

__str:__ 

*  a collection of one or more characters, e.g,. `"hello"`

## bool

__bool:__

*  either `True` or `False`

## bytearray

## tuple

__tuple:__

*  ordered collection of one or more data items, not necessarily of the same type, in parentheses.`(1,2,3,4)`

## list

__list:__

* ordered collection of one or more data items, not necessarily of the same time, put in square brackets, e,g,. `[1,2,3,4]`

## dictionary

__dictionary:__

* unordered collection of data in a key: value pair form, e.g., `{1: 'motor', 2: 'sensor'}`

# Constants

The following constants are obtained from the hub library

## hub

<span class='shell_output'>
hub.TOP = 0
hub.FRONT = 1
hub.RIGHT = 2
hub.BOTTOM = 3
hub.BACK = 4
hub.LEFT = 5
</span>

## Battery

<span class='shell_output'>
hub.battery.BATTERY_VOLTAGE_TOO_LOW=-5  
hub.battery.BATTERY_BAD_BATTERY=-4
hub.battery.BATTERY_TEMPERATURE_SENSOR_FAIL=-3
hub.battery.BATTERY_TEMPERATURE_OUT_OF_RANGE=-2
hub.battery.BATTERY_HUB_TEMPERATURE_CRITICAL_OUT_OF_RANGE=-2
hub.battery.BATTERY_NO_ERROR=0
</span>

<span class='shell_output'>
hub.battery.CHARGER_STATE_FAIL=-1  
hub.battery.CHARGER_STATE_DISCHARGING=0
hub.battery.CHARGER_STATE_CHARGING_ONGOING=1  
hub.battery.CHARGER_STATE_CHARGING_COMPLETED=2
</span>

<span class='shell_output'>
hub.battery.USB_CH_PORT_NONE=0
hub.battery.USB_CH_PORT_SDP=1
hub.battery.USB_CH_PORT_CDP=2
hub.battery.USB_CH_PORT_DCP=3               
</span>

## Image

build in images:
<span class='shell_output'>
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
</span>

## Sound

Waveforms
<span class='shell_output'>
hub.sound.SOUND_SIN=0       
hub.sound.SOUND_SQUARE=1
hub.sound.SOUND_TRIANGLE=2
hub.sound.SOUND_SAWTOOTH=3
</span>

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
possible gestures:

<span class='shell_output'>
hub.motion.TAPPED=0
hub.motion.DOUBLETAPPED=1
hub.motion.SHAKE=2
hub.motion.FREEFALL=3
</span>

### Port

<span class='shell_output'>
hub.port.ATTACED = 1
hub.port.DETACHED = 0
</span>

<span class='shell_output'>
hub.port.MODE_DEFAULT = 0
hub.port.MODE_FULL_DUPLEX = 1
hub.port.MODE_HALF_DUPLEX = 2
hub.port.MODE_GPIO = 3
</span>


### Motors

<span class='shell_output'>
hub.port.A.motor.BUSY_MODE = 0
hub.port.A.motor.BUSY_MOTOR = 1
</span>


<span class='shell_output'>
hub.port.A.motor.EVENT_COMPLETED = 0
hub.port.A.motor.EVENT_INTERRUPTED = 1
</span>

<span class='shell_output'>
hub.port.A.motor.FORMAT_RAW = 0
hub.port.A.motor.FORMAT_PCT = 1
hub.port.A.motor.FORMAT_SI = 2
</span>

<span class='shell_output'>
hub.port.A.motor.PID_POSITION = 0
hub.port.A.motor.PID_SPEED = 1
</span>


<span class='shell_output'>
hub.port.A.motor.STOP_FLOAT = 0
hub.port.A.motor.STOP_BRAKE = 1
hub.port.A.motor.STOP_HOLD = 2
</span>


## Sensors



