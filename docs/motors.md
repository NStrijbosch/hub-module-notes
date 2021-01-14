The motor class is a sub class of the [port](port.md) class which allows to control PU motors. It can be used via `motor=hub.port.A.motor`, see the examples below for more details. 

# Measurements

## get()

`motor.get()`

Measure sensor data from the motor. The specific measurements (speed, relative position, absolute position, power, load) depend on the mode of the motor, see [mode](#mode) for details to change mode, and [motors](#motors) for details on the default and available modes of each motor. 

__Returns:__

*  list of measurement data depending on the mode of the motor.

### sample code: read measurmenet data from motor connected to port A
``` python
from hub import port

MotorA = port.A.motor

MotorA.mode(3)          # Absolute position mode
abs_pos = MotorA.get()[0]
print("Absolute position: " + str(abs_pos))

Motor.mode([(1, 0), (2, 2)])  #Speed in RAW units and relative position in SI units
measurements = MotorA.get()
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

`motor.pwm(duty_cycle)`

Turn on motor with a given duty cycle

__Parameters:__

*  __duty_cycle__ [int](data_types.md#int) percentage of a cycle for which the signal is high. Value in range -100 ... 100.


### sample-code: turn on motor connected to port A
``` python
from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.pwm(40)      # start motor
sleep_ms(1000)      # wait 1 second
MOtorA.pwm(0)       # stop motor
```

## run_at_speed()

`motor.run_at_speed(speed=50, max_power=100, acceleration=100, deceleration=100, stall=False)`

Turn on motor with given speed.

__Parameters:__

*  __speed__ ([int](data_types.md#int)): desired velocity as percentage of maximum velocity. Value in range -100 ... 100.
*  __max_power__ ([int](data_types.md#int)): maximum power consumption as percentage of the maximum. Value in range 0 ... 100.
*  __acceleration__ ([int](data_types.md#int)): maximum accleration to reach desired velocity as percentage of maximum acceleration. Value in range 0 ... 100
*  __deceleration__ ([int](data_types.md#int)): maximum deceleration to reach desired velocity as percentage of maximum deceleration. Value in range 0 ... 100
*  __stall__ ([bool](data_types.md#bool)): `True`: stop when motor stall is detected; `False`: do not stop when motor stall is detected

## run_for_time()

`motor.run_for_time(time, speed=50, max_power=100, acceleration=100, deceleration=100, stall=False)`

Turn on motor for given time with given speed

__Parameters:__

*  __time__ in milliseconds ([int](data_types.md#int)): time to turn the motor on
*  __speed__ ([int](data_types.md#int)): desired velocity as percentage of maximum velocity. Value in range -100 ... 100.
*  __max_power__ ([int](data_types.md#int)): maximum power consumption as percentage of the maximum. Value in range 0 ... 100.
*  __acceleration__ ([int](data_types.md#int)): maximum accleration to reach desired velocity as percentage of maximum acceleration. Value in range 0 ... 100
*  __deceleration__ ([int](data_types.md#int)): maximum deceleration to reach desired velocity as percentage of maximum deceleration. Value in range 0 ... 100
*  __stall__ ([bool](data_types.md#bool)): `True`: stop when motor stall is detected; `False`: do not stop when motor stall is detected

## run_for_degrees()

`motor.run_for_degrees(degrees, speed=50, stall=True, acceleration=100, deceleration=100, stop=1)`

Turn motor a given number of degrees from current position

__Parameters:__

*  __position__ ([int](data_types.md#int)): desired number of degrees to turn. 
*  __speed__ ([int](data_types.md#int)): desired speed as percentage of maximum velocity. Value in range -100 ... 100.
*  __stall__ ([bool](data_types.md#bool)): `True`: stop when motor stall is detected; `False`: do not stop when motor stall is detected
*  __acceleration__ ([int](data_types.md#int)): maximum accleration to reach desired velocity as percentage of maximum acceleration. Value in range 0 ... 100
*  __deceleration__ ([int](data_types.md#int)): maximum deceleration to reach desired velocity as percentage of maximum deceleration. Value in range 0 ... 100
*  __stop__ ([int](data_types.md#int)): stop action after reaching target: STOP_FLOAT=0; STOP_BRAKE=1; STOP_HOLD=2.

## run_to_position()

`motor.run_to_position(position, speed=50, stall=True, acceleration=100, deceleration=100, stop=1)`

Turn motor to given relative position with given speed. 

> The position is relative to the position of the motor since starting the hub/connecting the motor. Best practice is to preset the position at the the start of a program

__Parameters:__

*  __position__ ([int](data_types.md#int)): desired relative position in degrees. 
*  __speed__ ([int](data_types.md#int)): desired speed as percentage of maximum velocity. Value in range -100 ... 100.
*  __stall__ ([bool](data_types.md#bool)): `True`: stop when motor stall is detected; `False`: do not stop when motor stall is detected
*  __acceleration__ ([int](data_types.md#int)): maximum accleration to reach desired velocity as percentage of maximum acceleration. Value in range 0 ... 100
*  __deceleration__ ([int](data_types.md#int)): maximum deceleration to reach desired velocity as percentage of maximum deceleration. Value in range 0 ... 100
*  __stop__ ([int](data_types.md#int)): stop action after reaching target: STOP_FLOAT=0; STOP_BRAKE=1; STOP_HOLD=2.

### sample code: Turn motor connected to port A in paralled to motor connected to port B

``` python
from hub import port

MotorA = port.A.motor
MotorB = port.B.motor

MotorA.mode(3)  # set mode to absolute position
MotorB.mode(3)  # set mode to absolute position

MotorA.preset(Motor.A.get()[0])  # preset 0 position to absolute zero position
MotorB.preset(Motor.B.get()[0])  # preset 0 position to absolute zero position

# Turn motors to different positions in parallel
MotorA.run_to_position(100,speed=50, stop = motorA.STOP_FLOAT)
MotorB.run_to_position(-200,speed=50)
```

## float()
`motor.float()`

Coast motor from current position

## brake()
  
`motor.brake()`

Brake at current position, after applying brake the motor floats. 

## hold()

`motor.hold()`

Hold at motor current position, motor is actively controlled to stay at current position.

# Settings

## pair()

`motor.pair(motor)`

__Parameters:__

*  motor to pair, e.g. hub.port.A.motor

## pid()

`motor.pid(p,i,d) `
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

## mode()

`hub.port.A.motor.mode(mode)`

Set mode of the motor. This only affects result of get() callback

__Parameters:__

*  mode: either a single mode (0,1,2,...) or array of modes ([(mode_1,format),(mode_2,format),(3,4)])

## default()

`hub.port.A.motor.default(pid=(0, 0, 0), max_power=0, speed=0, stall=True, deceleration=150, stop=1, callback=<bound_method>, acceleration=100})`

Set default settings of the motor

__Parameters:__
*  pid
*  max_power
*  speed
*  stall
*  deceleration
*  stop
*  callback
*  acceleration

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
