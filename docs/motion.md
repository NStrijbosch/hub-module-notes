
The motion class controls all functions linked to the internal IMU of the hub. It can read accelerometer data, gyro rates, yaw pitch and roll and detect gestures applied to the hub. It can be used via `hub.motion`.

# Gyro/Accelerometer Sensor Data

The hub can measure acceleration, yaw rate, and rotation directly from the IMU using the following commands.

## accelerometer()

`motion.accelerometer()`

Measure acceleration in each of the three-axis

__Returns:__

* [accleration x [int](data_types.md#int), accleration y [int](data_types.md#int), accleration z [int](data_types.md#int)]: acceleration in x,y,z direction with unknown unit.

__Sample code:__

``` python
from hub import motion

accelerations = motion.accelerometer()

print("a_x: " str(acclerations[0]) + " a_y: " str(acclerations[1]) + " a_z: " str(acclerations[2]) )
```

```
a_x: 1000 a_y: 0 a_z: 0
```

## gyroscope()

`motion.gyroscope()`

Measure rotational rates around each of the three axis

__Returns:__

* [rate x [int](data_types.md#int), rate y [int](data_types.md#int), rate z [int](data_types.md#int)]: rotational rate in x,y,z direction with unknown unit.

__Sample code:__

``` python
from hub import motion

rates = motion.gyroscope()

print("r_x: " str(rates[0]) + " r_y: " str(rates[1]) + " r_z: " str(rates[2]) )
```

```
r_x: 0 r_y: 0 r_z: 0
```

## yaw_pitch_roll()

`motion.yaw_pitch_roll()`

Measure rotation compared to fixed world. 

> In previews firmware versions this was `motion.position()`

__Returns:__

* [angele yaw [int](data_types.md#int), angle pitch [int](data_types.md#int), angle roll [int](data_types.md#int)]: yaw pitch and roll in degrees

__Sample code:__

``` python
from hub import motion

rotations = motion.yaw_pitch_roll()

print("yaw: " str(rotations[0]) + " pitch: " str(rotations[1]) + " roll: " str(rotations[2]) )
```

```
yaw: 0 pitch: 0 roll: 0
```

# Gestures

The hub can detect both the orientation or movement using the build in gyroscope and accelerometer

## orientation()  

`motion.orientation()'

__Returns:__

* orientation: which of the sides of the hub is facing upwards   
    TOP = 0  
    FRONT = 1  
    RIGHT = 2  
    BOTTOM = 3  
    BACK = 4  
    LEFT = 5  

__Sample code:__

``` python
from hub import motion

print('Orientation: ' + str(motion.orientation()))
```

## gesture()

`motion.gesture(gesture)`

Check if gesture is currently applied

__Parameters:__

* gesture ([int](data_types.md#int))
    TAPPED=0  
    DOUBLETAPPED=1  
    SHAKE=2  
    FREEFALL=3  

__Returns:__

* [bool](data_types.bool): `True` if input gesture is active, otherwise `False`.

__Sample code:__

``` python
from hub import motion

if motion.gesture(2):
    print("Hub is shaking!")
else:
    print("Hub is not shaking")
```
  

## (was_gesture())

`motion.gesture(gesture)`

Check if gesture was applied since last call

>  Missing from SPIKE firmware since 1.3.3

__Parameters:__

* gesture ([int](data_types.md#int))
    TAPPED=0  
    DOUBLETAPPED=1  
    SHAKE=2  
    FREEFALL=3  

__Returns:__

* [bool](data_types.bool): `True` if input gesture was active, otherwise `False`.

__Sample code:__

``` python
from hub import motion
from utime import sleep_ms

motion.was_gesture(0)  #first do a call, behaviour before current program is unknown

sleep_ms(2000)
print("Tap the hub")

if motion.was_gesture(0):
    print("Hub was tapped")
else:
    print("Hub was not tapped")
```

## align_to_model() TODO

`motion.align_to_model(angle?, angle?)`

align axis to align with robot (more tests necessary)

