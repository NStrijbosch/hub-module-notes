
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
|| | 
|-|-|
|Parameters:| [gesture](gesture) (optional) | 
|Returns: |  [bool](bool) or [gesture](gesture) 
| |  [bool](bool): observed  [gesture](gesture)  (if no  [gesture](gesture)  provided) | true if input [gesture](gesture) is currently observed |
| |  [gesture](gesture): observed  [gesture](gesture)  (if no  [gesture](gesture)  provided) |

```
hub.motion.was_gesture(gesture) 
```


|| | 
|-|-|
|Parameters:| [gesture](gesture) (optional) | 
|Returns: |  [bool](bool) or [gesture](gesture) 
| |  [bool](bool): observed  [gesture](gesture)  (if no  [gesture](gesture)  provided) | true if input [gesture](gesture) is observed since last call|
| |  [gesture](gesture): observed  [gesture](gesture)  (if no  [gesture](gesture)  provided) |


possible gestures:
leftside
rightside
down
up
front
back
tapped
doubletapped
shake
freefall