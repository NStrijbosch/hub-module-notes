<style type='text/css'>
.section ul { list-style: none !important; margin-left: 80px; margin-top:-3em;}
.section li { list-style: none !important}
.toctree-l2 a {margin-left: 0em;}
.toctree-l3 {margin-left: 2em;}
h2 {font-size: 125%;}
h2 {font-size: 115%;}
</style>



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

# Measurements

```
hub.port.A.motor.get()
```

For SP motors
__Returns:__

* [power,speed,pos,absolute pos] 

For other motors

__Returns:__
*  power if mode = 0
*  speed if mode = 1
*  relative position if mode = 2
*  absolute position if mode = 3 

```
hub.port.A.motor.busy()
```
Paramter:
hub.port.A.motor.BUSY_MODE or hub.port.A.motor.BUSY_MOTOR

if BUSY_MOTOR:
returns TRUE if target not achieved
returns FALSE if tracking not active

# Actions

## pwm()

```
hub.port.A.motor.pwm(duty cycle)
```

Turn on motor with given duty cycle

__Parameters:__

*  [duty_cycle][(data_types.md/#duty_cycle) the amount of time the signal is in a high (on) state as a percentage of the total time of it takes to complete one cycle. Integer value in range -100 ... 100)

## run_at_speed()

```
hub.port.A.motor.run_at_speed(speed,max_power,acceleration,100,stall)
```
Turn on motor with given speed

__Parameters:__

*  speed
*  maximum power
*  max acceleration
*  ?
*  stall 

## run_for_degrees()

```
hub.port.A.motor.run_for_degrees(degrees,speed)
```
Turn on motor with given number of degrees with given speed

__Parameters:__

*  degrees
*  speed

## run_to_position()

```
hub.port.A.motor.run_to_position(position,speed,acceleration?,stop action)
```

Turn motor to given _absolute?_ position with given speed

stop action: float=0,  brake=1, hold =2

__Parameters:__

*  position _absolute?_ position

> Test if this is absolute position. What does this mean for technic motors?

## run_for_time()

```
hub.port.A.motor.run_for_time(time,speed)
```
Turn motor on for given time with given speed

__Parameters:__

*  time (ms)
*  speed

## float()
```
hub.port.A.motor.float()
```
Coast motor from current position

## brake()
  
```
hub.port.A.motor.brake()
```
Brake at current position

> test what this means with respect to hold at current position

## Hold

```
hub.port.A.motor.hold()
```
Hold at motor current position

# Settings

```
hub.port.A.motor.pair(motor)
```
parameters: hub.port.X.motor

```
hub.port.A.motor.pid(p,i,d)
```

```
hub.port.A.motor.preset(hub.port.A.motor.FORMAT_X)
```

```
hub.port.A.motor.default()
```

```
hub.port.A.motor.mode(mode)
```
