The motor class is a sub class of the [port](port.md) class which allows to control all PU motors. It can be used via `motor=hub.port.A.motor`, see the examples below for more details. 

# Motor settings

---

## default()

`motor.default(pid=(0, 0, 0), max_power=0, speed=0, stall=True, deceleration=150, stop=1, callback=<bound_method>, acceleration=100})`

Set the default values of the motor settings. These values will be used when the settings are not given in one of the [actions](#actions) methods. 

__Parameters:__

*  __pid__ ([tuple](data_types.md#tuple)): PID gain (does not seem to have any effect)
*   __max_power__ ([int](data_types.md#int)): maximum power consumption as percentage of the maximum. Value in range 0 ... 100.
*   __speed__ ([int](data_types.md#int)): desired speed as percentage of maximum velocity. Value in range -100 ... 100.
*  __stall__ ([bool](data_types.md#bool)): `True`: stop when motor stall is detected; `False`: do not stop when motor stall is detected (not sure if this works)
*  __acceleration__ ([int](data_types.md#int)): maximum accleration to reach desired velocity as percentage of maximum acceleration. Value in range 0 ... 100
*  __deceleration__ ([int](data_types.md#int)): maximum deceleration to reach desired velocity as percentage of maximum deceleration. Value in range 0 ... 100
*  __stop__ ([int](data_types.md#int)): stop action after reaching target: STOP_FLOAT=0; STOP_BRAKE=1; STOP_HOLD=2.
*  __calLback__ : unknown

__Returns:__

*  [dictionary](data_types.md#dictionary): list of current default motor settings

__Sample code:__

``` python
from hub import port

MotorA = port.A.motor

MotorA.default(max_power = 50, stop = 2) #set max power to 50 and stop action to hold
print("default settings: " + str(MotorA.default()))
```

<span class='shell_output'>
\> default settings: {'pid': (0, 0, 0), 'max_power': 50, 'speed': 0, 'stall': True, 'deceleration': 150, 'stop': 2, 'callback': None, 'acceleration': 100}
</span>
  
---

## mode()

`hub.port.A.motor.mode(mode)`

Set mode of the motor, see [motors](#motors) for details on the default and available modes of each motor. This method only affects result of [get()](#get) callback.

__Parameters:__

*  mode can be one of the following:
  ([int](data_types.md#int)): a single mode, i.e., [get()](#get) will only return one measurement  
  ([tuple](data_types.md#tuple)): `(mode (int),unit (int))`, a single mode including its unit. Possible units: FORMAT_RAW = 0, FORMAT_PCT = 1,FORMAT_SI = 2.  
  ([list](data_types.md#int)): `[(mode1 (int),unit1 (int)),(mode2 (int),unit2 (int)), ...]` a list of multiple modes either as [int](data_types.md#int) or [tuple](data_types.md#tuple). 

__Returns:__

*  current mode. Only if no mode is given as parameter.

__Sample code:__

``` python
from hub import port

MotorA = port.A.motor

MotorA.mode(3)              # Set motor mode to absolute position
MotorA.mode((3,0))          # Set motor mode to absolute position in RAW units
MotorA.mode([3,2])          # Set motor mode to absolute position and relative position
MotorA.mode([(3,0),(2,2)])  # Set motor mode to absolute position in RAW units 
                            #   and relative position in SI units

print("Mode motor port A: " + str(MotorA.mode()))
``` 

<span class='shell_output'>
\> Mode motor port A: [(3,0),(2,2)]
</span>

## preset()

`motor.preset(position)`

Preset the value of the relative position

__Paramters:__

*  position ([int](data_types.md#int)): best practice is to use current position, or absolute position

__Sample code:__

``` python
from hub import port

MotorA = port.A.motor

MotorA.preset(100)
```

## pid()

`motor.pid(p,i,d) `

set controller gains of the PID controller. 

> The applied values of the actual controller do not seem to change.

__Parameters:__

*  p ([int](data_types.md#int)): proportional gain
*  i ([int](data_types.md#int)): integral gain
*  d ([int](data_types.md#int)): derivative gain

__Sample code:__

``` python
from hub import port

MotorA = port.A.motor

MotorA.pid(100,100,100)
```

# Measurements

## get()

`motor.get()`

Measure sensor data from the motor. The specific measurements (speed, relative position, absolute position, power, load) depend on the mode of the motor, see [mode](#mode) for details to change mode, and [motors](#motors) for details on the default and available modes of each motor. 

__Returns:__

*  list of measurement data depending on the mode of the motor.

__Sample code:__

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

<span class='shell_output'>
\> Absolute position: -2
\> Speed : 0 Relative position: 100
</span>

# Actions

## pwm()

`motor.pwm(duty_cycle)`

Turn on motor with a given duty cycle

__Parameters:__

*  __duty_cycle__ ([int](data_types.md#int)) percentage of a cycle for which the signal is high. Value in range -100 ... 100.


__Sample code:__

``` python
from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.pwm(40)    # start motor
sleep_ms(1000)    # wait 1 second
MotorA.pwm(0)     # stop motor
```

## run_at_speed()

`motor.run_at_speed(speed=50, max_power=100, acceleration=100, deceleration=100, stall=False)`

Turn on motor with given speed.

__Parameters:__

*  __speed__ ([int](data_types.md#int)): desired velocity as percentage of maximum velocity. Value in range -100 ... 100.
*  __max_power__ ([int](data_types.md#int)): maximum power consumption as percentage of the maximum. Value in range 0 ... 100.
*  __acceleration__ ([int](data_types.md#int)): maximum accleration to reach desired velocity as percentage of maximum acceleration. Value in range 0 ... 100
*  __deceleration__ ([int](data_types.md#int)): maximum deceleration to reach desired velocity as percentage of maximum deceleration. Value in range 0 ... 100
*  __stall__ ([bool](data_types.md#bool)): `True`: stop when motor stall is detected; `False`: do not stop when motor stall is detected (not sure if this works)


__Sample code:__

``` python
from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.run_at_speed(speed=50)   # turn motor at speed 50
sleep_ms(1000)                  # wait 1000 millisecond
MotorA.run_at_speed(0)          # turn motor at speed 0, i.e., stop
```

## run_for_time()

`motor.run_for_time(time, speed=50, max_power=100, acceleration=100, deceleration=100, stall=False)`

Turn on motor for given time with given speed

__Parameters:__

*  __time__ in milliseconds ([int](data_types.md#int)): time to turn the motor on
*  __speed__ ([int](data_types.md#int)): desired velocity as percentage of maximum velocity. Value in range -100 ... 100.
*  __max_power__ ([int](data_types.md#int)): maximum power consumption as percentage of the maximum. Value in range 0 ... 100.
*  __acceleration__ ([int](data_types.md#int)): maximum accleration to reach desired velocity as percentage of maximum acceleration. Value in range 0 ... 100
*  __deceleration__ ([int](data_types.md#int)): maximum deceleration to reach desired velocity as percentage of maximum deceleration. Value in range 0 ... 100
*  __stall__ ([bool](data_types.md#bool)): `True`: stop when motor stall is detected; `False`: do not stop when motor stall is detected (not sure if this works)

__Sample code:__

``` python
from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.run_for_time(1000,speed=50)   # turn motor for 1000 milliseconds at speed 50
```

## run_for_degrees()

`motor.run_for_degrees(degrees, speed=50, max_power=100, stall=True, acceleration=100, deceleration=100, stop=1)`

Turn motor a given number of degrees from current position

__Parameters:__

*  __position__ ([int](data_types.md#int)): desired number of degrees to turn. 
*  __speed__ ([int](data_types.md#int)): desired speed as percentage of maximum velocity. Value in range -100 ... 100.
*   __max_power__ ([int](data_types.md#int)): maximum power consumption as percentage of the maximum. Value in range 0 ... 100.
*  __stall__ ([bool](data_types.md#bool)): `True`: stop when motor stall is detected; `False`: do not stop when motor stall is detected (not sure if this works)
*  __acceleration__ ([int](data_types.md#int)): maximum accleration to reach desired velocity as percentage of maximum acceleration. Value in range 0 ... 100
*  __deceleration__ ([int](data_types.md#int)): maximum deceleration to reach desired velocity as percentage of maximum deceleration. Value in range 0 ... 100
*  __stop__ ([int](data_types.md#int)): stop action after reaching target: STOP_FLOAT=0; STOP_BRAKE=1; STOP_HOLD=2.

__Sample code:__
```python
from hub import port

MotorA = port.A.motor
MotorB = port.B.motor

# Turn motors to different positions in parallel
MotorA.run_for_degrees(100,speed=50)
MotorB.run_for_degrees(-400,speed=50)
```

## run_to_position()

`motor.run_to_position(position, speed=50, max_power=100, stall=True, acceleration=100, deceleration=100, stop=1)`

Turn motor to given relative position with given speed. 

> The position is relative to the position of the motor since starting the hub/connecting the motor. Best practice is to preset the position at the the start of a program

__Parameters:__

*  __position__ ([int](data_types.md#int)): desired relative position in degrees. 
*  __speed__ ([int](data_types.md#int)): desired speed as percentage of maximum velocity. Value in range -100 ... 100.
*   __max_power__ ([int](data_types.md#int)): maximum power consumption as percentage of the maximum. Value in range 0 ... 100.
*  __stall__ ([bool](data_types.md#bool)): `True`: stop when motor stall is detected; `False`: do not stop when motor stall is detected (not sure if this works)
*  __acceleration__ ([int](data_types.md#int)): maximum accleration to reach desired velocity as percentage of maximum acceleration. Value in range 0 ... 100
*  __deceleration__ ([int](data_types.md#int)): maximum deceleration to reach desired velocity as percentage of maximum deceleration. Value in range 0 ... 100
*  __stop__ ([int](data_types.md#int)): stop action after reaching target: STOP_FLOAT=0; STOP_BRAKE=1; STOP_HOLD=2.

__Sample code:__

``` python
from hub import port

MotorA = port.A.motor

MotorA.mode(2)# set mode to absolute position

MotorA.preset(MotorA.get()[0])# preset 0 position to absolute zero position

# Turn motors to different positions in parallel
MotorA.run_to_position(180,speed=50)
```

## float()

`motor.float()`

Coast motor from current position

__Sample code:__

``` python
from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.pwm(40)      # start motor
sleep_ms(1000)      # wait 1 second
MotorA.float()      # float motor
```

## brake()
  
`motor.brake()`

Brake at current position, after applying brake the motor floats. 

__Sample code:__

``` python
from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.pwm(40)      # start motor
sleep_ms(1000)      # wait 1 second
MotorA.brake()      # apply brake
```

## hold()

`motor.hold()`

Actively hold the motor at its current position.

__Sample code:__

``` python
from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.pwm(40)     # start motor
sleep_ms(1000)     # wait 1 second
MotorA.hold()      # actively hold position
sleep_ms(10000)    # wait 10 second active resistance should be noticable
MotorA.float()     # float motor
```

## busy()

`port.A.motor.busy(type)`

__Parameters:__

*  type [int](data_types.md#int): which type of busy:  
   0: busy mode ?(yet unknown meaning)
   1: busy motor (target not reached or not)

__Returns:__

*  TRUE if busy, FALSE if not busy

__Sample code:__

```python
from hub import port
from utime import sleep_ms

from hub import port

MotorA = port.A.motor
MotorB = port.B.motor

# Turn motors to different positions in parallel
MotorA.run_for_degrees(100,speed=50)
MotorB.run_for_degrees(-400,speed=50)

while MotorA.busy(1) or MotorB.busy(1):
    sleep_ms(10)

print('Both motors reached their target')

```

## pair()

`motorA.pair(motorB)`

Pair two motors. Both motors can now be controlled via motorA (even with different speeds). 

__Parameters:__

*  motor to pair, e.g., port.B.motor()

__Sample code:__

``` python
from hub import port

MotorA = port.A.motor
MotorB = port.B.motor

Pair=MotorA.pair(MotorB)

Pair.run_for_degrees(270, 100, 50) # Motor A turns 360 and Motor B turns 180
                                   # Combined distance = 2*270
```

# Motor Modes

All motors with rotation sensor have the following modes


|Mode|Name |RAW |      |PCT |      |SI  |      |Symbol|Capabilities?           |Datasets|Type|Figures|Decimals|
|----|-----|----|------|----|------|----|------|------|------------------------|--------|----|-------|--------|
|0   |POWER (pwm)|-100|100   |-100|100   |-100|100   |PCT   |\x10\x00\x00\x00\x01\x04|1       |0   |1      |0       |
|1   |SPEED (rotation rate)|-100|100   |-100|100   |-100|100   |PCT   |\x10\x00\x00\x00\x01\x04|1       |0   |4      |0       |
|2   |POS  (relative rotation)|-360|360   |-100|100   |-360|360   |DEG   |\x10\x00\x00\x00\x01\x04|1       |2   |4      |0       |
|3   |APOS (absolute rotation)|-180|179   |-200|200   |-180|-179  |DEG   |\x10\x00\x00\x00\x01\x04|1       |1   |3      |0       |
|4   |LOAD (load) |0   |127   |0   |100   |0   |127   |PCT   |\x10\x00\x00\x00\x01\x04|1       |1   |1      |0       |

The default mode of the Large/Medium Angular motor is: (see [mode](#mode) for more details)

<span class='shell_output'>
\> Default mode: [(1, 0), (2, 2), (3, 1), (0, 0)]
</span>
