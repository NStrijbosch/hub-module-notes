
# Motion class

## Data types

### gesture

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
* [gesture](gesture) (optional)


Returns:
* [bool](bool) (if [gesture](gesture) provided) or [gesture](gesture)
  * [bool](bool): true if input [gesture](gesture) is active
  * [gesture](gesture): the active  [gesture](gesture)

```
hub.motion.was_gesture(gesture) 
```
Parameters:

* [gesture](gesture)


Returns:
<ol>
<li> [bool](bool): true if input [gesture](gesture) is active since last call </li>
</ol>