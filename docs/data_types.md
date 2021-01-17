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
hub.TOP = 0 </br>
hub.FRONT = 1</br>
hub.RIGHT = 2</br>
hub.BOTTOM = 3</br>
hub.BACK = 4</br>
hub.LEFT = 5
</span>

## Battery

<span class='shell_output'>
hub.battery.BATTERY_VOLTAGE_TOO_LOW=-5  </br>
hub.battery.BATTERY_BAD_BATTERY=-4</br>
hub.battery.BATTERY_TEMPERATURE_SENSOR_FAIL=-3</br>
hub.battery.BATTERY_TEMPERATURE_OUT_OF_RANGE=-2</br>
hub.battery.BATTERY_HUB_TEMPERATURE_CRITICAL_OUT_OF_RANGE=-2</br>
hub.battery.BATTERY_NO_ERROR=0
</span>

<span class='shell_output'>
hub.battery.CHARGER_STATE_FAIL=-1  </br>
hub.battery.CHARGER_STATE_DISCHARGING=0</br>
hub.battery.CHARGER_STATE_CHARGING_ONGOING=1  </br>
hub.battery.CHARGER_STATE_CHARGING_COMPLETED=2
</span>

<span class='shell_output'>
hub.battery.USB_CH_PORT_NONE=0</br>
hub.battery.USB_CH_PORT_SDP=1</br>
hub.battery.USB_CH_PORT_CDP=2</br>
hub.battery.USB_CH_PORT_DCP=3               
</span>

## Image

build in images:
<span class='shell_output'>
hub.Image.ALL_ARROWS  </br>
hub.Image.ALL_CLOCKS</br>
hub.Image.ANGRY</br>
hub.Image.ARROW_E</br>
hub.Image.ARROW_N</br>
hub.Image.ARROW_NE</br>
hub.Image.ARROW_NW</br>
hub.Image.ARROW_S</br>
hub.Image.ARROW_SE</br>
hub.Image.ARROW_SW</br> 
hub.Image.ARROW_W</br>
hub.Image.ASLEEP</br>
hub.Image.BUTTERFLY</br>
hub.Image.CHESSBOARD</br>
hub.Image.CLOCK1</br>
hub.Image.CLOCK10</br>
hub.Image.CLOCK11</br>
hub.Image.CLOCK12</br>
hub.Image.CLOCK2</br>
hub.Image.CLOCK3</br>
hub.Image.CLOCK4</br>
hub.Image.CLOCK5</br>
hub.Image.CLOCK6</br>
hub.Image.CLOCK7</br>
hub.Image.CLOCK8 </br>
hub.Image.CLOCK9</br>
hub.Image.CONFUSED</br>
hub.Image.COW</br>
hub.Image.DIAMOND</br>
hub.Image.DIAMOND_SMALL</br>
hub.Image.DUCK</br>
hub.Image.FABULOUS</br>
hub.Image.GHOST</br>
hub.Image.GIRAFFE</br>
hub.Image.GO_DOWN</br>
hub.Image.GO_LEFT</br>
hub.Image.GO_RIGHT</br>
hub.Image.GO_UP</br>
hub.Image.HAPPY</br>
hub.Image.HEART</br>
hub.Image.HEART_SMALL</br>
hub.Image.HOUSE</br>
hub.Image.MEH</br>
hub.Image.MUSIC_CROTCHET</br>
hub.Image.MUSIC_QUAVER</br>
hub.Image.MUSIC_QUAVERS</br>
hub.Image.NO</br>
hub.Image.PACMAN</br>
hub.Image.PITCHFORK</br>
hub.Image.RABBIT</br>
hub.Image.ROLLERSKATE</br>
hub.Image.SAD</br>
hub.Image.SILLY</br>
hub.Image.SKULL</br>
hub.Image.SMILE</br>
hub.Image.SNAKE</br>
hub.Image.SQUARE</br>
hub.Image.SQUARE_SMALL</br>
hub.Image.STICKFIGURE</br>
hub.Image.SURPRISED</br>
hub.Image.SWORD</br>
hub.Image.TARGET</br>
hub.Image.TORTOISE</br>
hub.Image.TRIANGLE</br>
hub.Image.TRIANGLE_LEFT</br>
hub.Image.TSHIRT</br>
hub.Image.UMBRELLA</br>
hub.Image.XMAS</br>
hub.Image.YES
</span>

## Sound

Waveforms
<span class='shell_output'>
hub.sound.SOUND_SIN=0</br>
hub.sound.SOUND_SQUARE=1</br>
hub.sound.SOUND_TRIANGLE=2</br>
hub.sound.SOUND_SAWTOOTH=3</br>
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
hub.motion.TAPPED=0</br>
hub.motion.DOUBLETAPPED=1</br>
hub.motion.SHAKE=2</br>
hub.motion.FREEFALL=3
</span>

### Port

<span class='shell_output'>
hub.port.ATTACED = 1</br>
hub.port.DETACHED = 0</br>
</span>

<span class='shell_output'>
hub.port.MODE_DEFAULT = 0</br>
hub.port.MODE_FULL_DUPLEX = 1</br>
hub.port.MODE_HALF_DUPLEX = 2</br>
hub.port.MODE_GPIO = 3
</span>


### Motors

<span class='shell_output'>
hub.port.A.motor.BUSY_MODE = 0</br>
hub.port.A.motor.BUSY_MOTOR = 1
</span>


<span class='shell_output'>
hub.port.A.motor.EVENT_COMPLETED = 0</br>
hub.port.A.motor.EVENT_INTERRUPTED = 1
</span>

<span class='shell_output'>
hub.port.A.motor.FORMAT_RAW = 0</br>
hub.port.A.motor.FORMAT_PCT = 1</br>
hub.port.A.motor.FORMAT_SI = 2
</span>

<span class='shell_output'>
hub.port.A.motor.PID_POSITION = 0</br>
hub.port.A.motor.PID_SPEED = 1
</span>

<span class='shell_output'>
hub.port.A.motor.STOP_FLOAT = 0</br>
hub.port.A.motor.STOP_BRAKE = 1</br>
hub.port.A.motor.STOP_HOLD = 2
</span>

## Sensors



