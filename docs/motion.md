
<style type='text/css'>
.section ul { list-style: none !important; margin-left: 80px; margin-top:-3em;}
.section li { list-style: none !important}
.toctree-l2 a {margin-left: 0em;}
.toctree-l3 {margin-left: 2em;}
h2 {font-size: 125%;}
h2 {font-size: 115%;}
</style>

# Gyro/Accelerometer Sensor Data

The hub can measure acceleration, yaw rate, and rotation directly from the gyroscope and accelerometer using the following commands


## accelerometer()

```
hub.motion.accelerometer()
```
__Returns:__

* [[acceleration](data_types.md#acceleration) x, [acceleration](data_types.md#acceleration) y, [acceleration](data_types.md#acceleration) z] acceleration in x,y,z direction

## accelerometer_filter()

```
hub.motion.accelerometer_filter()
```

__Returns:__

* [[acceleration](data_types.md#acceleration) x, [acceleration](data_types.md#acceleration) y, [acceleration](data_types.md#acceleration) z] acceleration in x,y,z direction

> Note: no difference observed in measurement data with respect to hub.motion.accelerometer()

## gyroscope()

```
hub.motion.gyroscope()
```
__Returns:__

* [[yaw rate](data_types.md#yaw) x, [yaw rate](data_types.md#yaw) y, [yaw rate](data_types.md#yaw) z] rotational rate around in x,y,z axis
  

## gyroscope_filter()

```
hub.motion.gyroscope_filter()
```
__Returns:__

* [[yaw rate](data_types.md#yaw) x, [yaw rate](data_types.md#yaw) y, [yaw rate](data_types.md#yaw) z] rotational rate around in x,y,z axis

> Note: no difference observed in measurement data with respect to hub.motion.gyroscope()

## position()

```
hub.motion.position()
```

__Returns:__

* [[angle](data_types.md#angle) x, [angle](data_types.md#angle) y, [angle](data_types.md#angle) z] rotation in degrees around x,y,z axis


# Gestures

The hub can detect both the orientation or movement using the build in gyroscope and accelerometer

## orientation()  

```
hub.motion.orientation()  
```

__Returns:__

* [gesture](data_types.md#gesture) 

## gesture(_[gesture](data_types.md#gesture)_)

```
hub.motion.gesture(gesture)
```
__Parameters:__

* [gesture](data_types.md#gesture)

__Returns:__

* [bool](data_types.bool): true if input [gesture](data_types.md#gesture) is active
  
## was_gesture(_[gesture](data_types.md#gesture)_) 

```
hub.motion.was_gesture(gesture) 
```
__Parameters:__

* [gesture](data_types.md#gesture)

__Returns:__

* [bool](data_types.bool): true if input [gesture](data_types.md#gesture) was active since last call



# To do
```
hub.motion.preset_yaw()
```
```
hub.motion.preset_yaw()
```
