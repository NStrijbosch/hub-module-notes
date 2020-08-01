
<style type='text/css'>
.section ul { list-style: none !important; margin-left: 80px; margin-top:-3em;}
.section li { list-style: none !important}
</style>

## Gyro/Accelerometer Sensor Data

```
hub.motion.accelerometer()
```
__Returns:__

* int[3] acceleration in x,y,z direction

```
hub.motion.accelerometer_filter()
```


__Returns:__

* int[3] acceleration in x,y,z direction

> Note: no difference observed with version with hub.motion.accelerometer()

```
hub.motion.gyroscope()
```
__Returns:__

* int[3] rotational rate around in x,y,z axis
  
```
hub.motion.gyroscope_filter()
```
__Returns:__

* int[3] rotational rate around x,y,z axis

> Note: no difference observed with version with hub.motion.gyroscope()

```
hub.motion.position()
```

__Returns:__

* int[3] rotation in degrees around x,y,z axis


## Gesture 

The hub can detect both the orientation or movement using the build in gyroscope and accelerometer

```
hub.motion.orientation()  
```

__Returns:__

* string referecing a [gesture](data_types.md#gesture) 


```
hub.motion.gesture(string)
```
__Parameters:__

* string referencing a [gesture](data_types.md#gesture) (optional)


__Returns:__

* [bool](bool): true if input [gesture](data_types.md#gesture) is active
  
```
hub.motion.was_gesture(string) 
```
__Parameters:__

* string referencing a [gesture](data_types.md#gesture)


__Returns:__

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