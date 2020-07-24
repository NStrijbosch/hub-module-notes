
# Motion

## Gyro/Accelerometer Sensor Data

```
hub.motion.accelerometer()
```
Parameters

* None

Returns:

* int[3] acceleration in x,y,z direction

```
hub.motion.accelerometer_filter()
```
Parameters

* None

Returns:

* int[3] acceleration in x,y,z direction

> Note: no difference observed with version with hub.motion.accelerometer()

```
hub.motion.gyroscope()
```
Parameters

* None

Returns:

* int[3] rotational rate around in x,y,z axis
  
```
hub.motion.gyroscope_filter()
```
Parameters

* None

Returns:

* int[3] rotational rate around x,y,z axis

> Note: no difference observed with version with hub.motion.gyroscope()

```
hub.motion.position()
```

Parameters:

* None

Returns:

* int[3] rotation in degrees around x,y,z axis


## Gesture 

The hub can detect both the orientation or movement using the build in gyroscope and accelerometer

possible gestures:

```
hub.motion.BACK
hub.motion.DOUBLETAPPED
hub.motion.DOWN
hub.motion.FREEFALL
hub.motion.FRONT
hub.motion.LEFTSIDE
hub.motion.NONE
hub.motion.RIGHTSIDE
hub.motion.SHAKE
hub.motion.TAPPED
hub.motion.UP
```

```
hub.motion.orientation()  
```

Parameters:

* None

Returns:

* string referecing a [gesture](data_types.md#gesture) 


```
hub.motion.gesture(string)
```
Parameters:
* string referencing a [gesture](data_types.md#gesture) (optional)


Returns:

* [bool](bool): true if input [gesture](data_types.md#gesture) is active
  
```
hub.motion.was_gesture(string) 
```
Parameters:

* string referencing a [gesture](data_types.md#gesture)


Returns:

* [bool](bool): true if input [gesture](data_types.md#gesture) is active since last call

### To do
```
hub.motion.preset_yaw()
```
```
hub.motion.preset_yaw()
```


asdfasdfalkasfasf </br>

&emsp;asdfasldflk </br>
&emsp;asdkfasld

rkdown Space Test with HTML Command

Normal text

&thinsp; Narrower than usual space

&nbsp; Usual space width

&ensp; Wider than usual space width

&emsp; Double wider than usual space


### Returns

&emsp; Name of the color </br>
&emsp; __type__: asdfasdfa </br>
&emsp; __values__: asdfasd

### Errors

&emsp; Name of the color </br>
&emsp; __type__: asdfasdfa </br>
&emsp; __values__: asdfasd