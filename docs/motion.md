# Gyro/Accelerometer Sensor Data

The hub can measure acceleration, yaw rate, and rotation directly from the gyroscope and accelerometer using the following commands


## accelerometer()

```
hub.motion.accelerometer()
```
__Returns:__

* [[acceleration](data_types.md#acceleration) x, [acceleration](data_types.md#acceleration) y, [acceleration](data_types.md#acceleration) z] acceleration in x,y,z direction


## gyroscope()

```
hub.motion.gyroscope()
```
__Returns:__

* [[yaw rate](data_types.md#yaw) x, [yaw rate](data_types.md#yaw) y, [yaw rate](data_types.md#yaw) z] rotational rate around in x,y,z axis
  

## (position())

```
hub.motion.position()
```

__Returns:__

* [[angle](data_types.md#angle) x, [angle](data_types.md#angle) y, [angle](data_types.md#angle) z] rotation in degrees around x,y,z axis

missing from SPIKE firmware since 1.3.3 -> alternative yaw_pitch_roll

## yaw_pitch_roll()

```
hub.motion.yaw_pitch_roll()
```

__Returns:__

* [[angle](data_types.md#angle) x, [angle](data_types.md#angle) y, [angle](data_types.md#angle) z] rotation in degrees around x,y,z axis

## align_to_model()

```
hub.motion.align_to_model(angle?, angle?)
```

align axis to align with robot (more test necessary)

# Gestures

The hub can detect both the orientation or movement using the build in gyroscope and accelerometer

## orientation()  

```
hub.motion.orientation()  
```

__Returns:__

* [orientation](data_types.md#orientation) 

## gesture()

```
hub.motion.gesture(gesture)
```
__Parameters:__

* [gesture](data_types.md#gesture)

__Returns:__

* [bool](data_types.bool): true if input [gesture](data_types.md#gesture) is active
  
## (was_gesture()) 

```
hub.motion.was_gesture(gesture) 
```
__Parameters:__

* [gesture](data_types.md#gesture)

__Returns:__

* [bool](data_types.bool): true if input [gesture](data_types.md#gesture) was active since last call

missing from SPIKE firmware since 1.3.3

