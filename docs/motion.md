
# Motion class

## Data types


## Gyro/Accelerometer Sensor

```
hub.motion.accelerometer()
```
Input: None

Output: 
```
hub.motion.gyroscope()
```

```
hub.motion.position()
```

```
hub.motion.orientation()  
```

## Gesture 

```
hub.motion.gesture(gesture)
```
Parameters:
* [gesture](data_types.md#gesture) (optional)


Returns:

* [bool](bool) (if parameter [gesture](data_types.md#gesture) provided) or [gesture](data_types.md#gesture)
    * [bool](bool): true if input [gesture](data_types.md#gesture) is active
    * [gesture](data_types.md#gesture): the active  [gesture](data_types.md#gesture)

```
hub.motion.was_gesture(gesture) 
```
Parameters:

* [gesture](data_types.md#gesture)


Returns:

* [bool](bool): true if input [gesture](data_types.md#gesture) is active since last call
