# Measurements

## get()


`hub.port.A.motor.get() `

``` 
'hallo'
asdfa
asd
x=10


```


The behaviour of this callback depends on the mode of the motor. 

__Returns:__

*  power if mode = 0
*  speed if mode = 1
*  relative position if mode = 2
*  absolute position if mode = 3 

For SP motors the default mode is ([(1, 0), (2, 2), (3, 1), (0, 0)]<=not correct need to check)
which returns in the following form:

__Returns:__

*  [power(PCT),speed(SI),pos(SI),absolute pos(RAW)] 


``` python
from hub import port

Motor = port.A.motor

Motor.mode(3)          # Absolute position mode
abs_pos = Motor.get()[0]
print("Absolute position: " + str(abs_pos))

Motor.mode([(1, 0), (2, 2)])  #Speed in RAW and relative position in SI
measurements = Motor.get()
print("Speed : " + str(measurements[0]) + " Relative position: " + str(measurements[1]))

```

``` python
>>> Absolute position: -20
>>> Speed : 0 Relative position: 0
```

## busy()

`hub.port.A.motor.busy()`

__Parameters:__

*  hub.port.A.motor.BUSY_MODE or hub.port.A.motor.BUSY_MOTOR

__Returns:__

*  TRUE if target not achieved, FALSE if tracking not active

# Actions

## pwm()

`hub.port.A.motor.pwm([int](data_types.md#int) duty_cycle)`

Turn on motor with given duty cycle

__Parameters:__

*  [duty_cycle][(data_types.md/#duty_cycle) the amount of time the signal is in a high (on) state as a percentage of the total time of it takes to complete one cycle. Integer value in range -100 ... 100)

## run_at_speed()

`hub.port.A.motor.run_at_speed(speed,max_power,acceleration,100,stall)`

Turn on motor with given speed

__Parameters:__

*  speed
*  maximum power
*  max acceleration
*  ?
*  stall 

## run_for_degrees()

`hub.port.A.motor.run_for_degrees(degrees,speed)`

Turn on motor with given number of degrees with given speed

__Parameters:__

*  degrees
*  speed

## run_to_position()

`hub.port.A.motor.run_to_position(position,speed,acceleration?,stop action)`

Turn motor to given relative position with given speed. 

> Position is the relative position since STARTING the hub. Best practice is to preset the position to the absolute position at the start of a program.

TODO: stop action: float=0,  brake=1, hold =2

__Parameters:__

*  relative position
*  speed
*  accelaration
*  deceleration
*  stop action

## run_for_time()

`hub.port.A.motor.run_for_time(time,speed)`

Turn motor on for given time with given speed

__Parameters:__

*  time (ms)
*  speed

## float()
`hub.port.A.motor.float()`

Coast motor from current position

## brake()
  
`hub.port.A.motor.brake()`

Brake at current position

> test what this means with respect to hold at current position

## hold()

`hub.port.A.motor.hold()`

Hold at motor current position

# Settings

## pair()

`hub.port.A.motor.pair(motor)`

__Parameters:__

*  motor to pair, e.g. hub.port.A.motor

## pid()

`hub.port.A.motor.pid(p,i,d) `
set controller gains of PID. 

> Does not seems to work

__Parameters:__

*  p: proportional gain
*  i: integral gain
*  d: derivative gain

## preset()

`hub.port.A.motor.preset(position)`
Preset the relative position

__Parameters:__

*  position: the position you want to be zero? -> TODO: formulation

## mode

`hub.port.A.motor.mode(mode)`

Set mode of the motor. This only affects result of get() callback

__Parameters:__

*  mode: either a single mode (0,1,2,...) or array of modes ([(mode_1,format),(mode_2,format),(3,4)])

## default()

`hub.port.A.motor.default()`


# Motors

### Medium Motor

hw_version = 4096
fw_version = 4096
combi_modes = (14,15)
type = 48

``` python
from hub import port

medium_motor = port.A.motor

default_mode = port.A.motor.mode()

print(default_mode)
```

```
>>> [(1, 0), (2, 2), (3, 1), (0, 0)]
```

|Mode|Name |RAW |      |PCT |      |SI  |      |Symbol|Capabilities?           |Datasets|Type|Figures|Decimals|
|----|-----|----|------|----|------|----|------|------|------------------------|--------|----|-------|--------|
|0   |POWER|-100|100   |-100|100   |-100|100   |PCT   |\x10\x00\x00\x00\x01\x04|1       |0   |1      |0       |
|1   |SPEED|-100|100   |-100|100   |-100|100   |PCT   |\x10\x00\x00\x00\x01\x04|1       |0   |4      |0       |
|2   |POS  |-360|360   |-100|100   |-360|360   |DEG   |\x10\x00\x00\x00\x01\x04|1       |2   |4      |0       |
|3   |APOS |-180|179   |-200|200   |-180|-179  |DEG   |\x10\x00\x00\x00\x01\x04|1       |1   |3      |0       |
|4   |LOAD |0   |127   |0   |100   |0   |127   |PCT   |\x10\x00\x00\x00\x01\x04|1       |1   |1      |0       |
