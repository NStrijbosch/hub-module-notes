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

## Commands 

```
hub.port.A.motor.mode(mode)
```

```
hub.port.A.motor.get()
```



```
hub.port.A.motor.float()
```
Float motor axle from current position

Parameters:

* None

Returns:

* None
  
```
hub.port.A.motor.brake()
```
Turn on brake of motor at current position

Parameters:

* None

Returns:

* None

```
hub.port.A.motor.hold()
```

Hold motor at current position

Parameters:

* None

Returns:

* None

## 
```
hub.port.A.motor.busy()
```
Paramter:
hub.port.A.motor.BUSY_MODE or hub.port.A.motor.BUSY_MOTOR


## Movement functions

```
hub.port.A.motor.pwm(pwm)
```
Parameters

* pwm (int in range -100 - 100)

Returns:

* None

```
hub.port.A.motor.run_at_speed(speed,max_power,acceleration,100,stall)
```

```
hub.port.A.motor.run_for_degrees(degrees,speed)
```

```
hub.port.A.motor.run_to_position(position,speed)
```

```
hub.port.A.motor.run_for_time(ms,speed)
```

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

<table>
    <tr>