The device class is a sub class of the [port](port.md) class which allows to control PU Sensor. It can be used via `sensor=hub.port.A.device`, see the examples below for more details. 


# General

## mode()

`device.mode(mode)`

Set mode of the sensor, see [sensors](#sensors) for details on the default and available modes of each sensor. This method only affects result of [get()](#get).

__Parameters:__

*  mode can be one of the following:
  ([int](data_types.md#int)): a single mode, i.e., [get()](#get) will only return one measurement  
  ([tuple](data_types.md#tuple)): `(mode (int),unit (int))`, a single mode including its unit. Possible units: FORMAT_RAW = 0, FORMAT_PCT = 1,FORMAT_SI = 2.  
  ([list](data_types.md#int)): `[(mode1 (int),unit1 (int)),(mode2 (int),unit2 (int)), ...]` a list of multiple modes either as [int](data_types.md#int) or [tuple](data_types.md#tuple). 

__Returns:__

*  current mode. Only if no mode is given as parameter.

__Sample code:__

``` python
from hub import port

SensorA = port.A.device

MotorA.mode(3)              # Set sensor to mode 3
MotorA.mode((3,0))          # Set sensor to mode 3 in RAW units
MotorA.mode([3,2])          # Set sensor to mode 3 and mode 2
MotorA.mode([(3,0),(2,2)])  # Set sensor to mode 3 in RAW units 
                            #   and mode 2 in SI units 

print("Mode sensor port A: " + str(MotorA.mode()))
``` 

``` python
>>> Mode sensor port A: [(3,0),(2,2)]
```

Some PU sensor modes allow to affect send data to the sensor. This can be achieved using the following

`device.mode(mode,data)`

__Parameters:__

*  mode ([int](data_types.md#int)): a single mode
*  data ([bytearray](data_types.md#bytearray)): data to be send

__Sample code:__

``` python
from hub import port

SensorA = port.A.device

SensorA.mode(5)  # first set the correct mode before sending data
SensorA.mode(5,b''+chr(3))
```

> See [Sensors](#sensors) for the specific modes where sending data is usefull for each sensor

---

## get()

`device.get()`

Obtain measurement data from the sensor depending on the mode of the motor, see [mode](#mode) for details to change mode, and [sensors](#sensors) for details on the default and available modes of each motor. 

__Returns:__

*  list of measurement data depending on the mode of the motor.

__Sample code:__

``` python
from hub import port

DistanceSensor = port.A.device

DistanceSensor.mode((1,0))          # Distance short in RAW units
distance = DistanceSensor.get()[0]
print("distance: " + str(distance))
```

``` python
>>> Distance: 20.0
```

# Sensors

## Ultrasonic Sensor
|Mode|Name |RAW          |PCT        |SI           |Symbol|Capabilities?       |Datasets|Type|Figures|Decimals|
|----|-----|-------------|-----------|-------------|------|--------------------|--------|----|-------|--------|
|0   |DISTL|0.0...2500.0 |0.0...100.0|0.0...250.0  |cm    |\x00\x00\x00\x04\x84|1       |1   |5      |1       |
|1   |DISTS|0.0...320.0  |0.0...100.0|0.0...32.0   |cm    |\x00\x00\x00\x04\x84|1       |1   |4      |1       |
|2   |SINGL|0.0...2500.0 |0.0...100.0|0.0...250.0  |cm    |\x00\x00\x00\x04\x84|1       |1   |5      |1       |
|3   |LISTN|0.0...1.0    |0.0...100.0|0.0...1.0    |ST    |\x00\x00\x00\x04\x84|1       |0   |1      |0       |
|4   |TRAW |0.0...14577.0|0.0...100.0|0.0...14577.0|us    |\x00\x00\x00\x04\x84|1       |2   |5      |0       |
|5   |LIGHT|0.0...100.0  |0.0...100.0|0.0...100.0  |pct   |\x00\x00\x04\x84    |4       |0   |3      |0       |
|6   |PING |0.0...1.0    |0.0...100.0|0.0...1.0    |pct   |\x80\x00\x00\x04\x84|1       |0   |1      |0       |
|7   |ADRAW|0.0...1024.0 |0.0...100.0|0.0...1024.0 |pct   |\x80\x00\x00\x04\x84|1       |1   |4      |0       |
|8   |CALIB|0.0...255.0  |0.0...100.0|0.0...255.0  |pct   |\x00\x00\x04\x84    |7       |0   |3      |0       |

```
hub.port.A.device.mode(mode, )
```


## Color Sensor

|Mode|Name |RAW |       |PCT|     |SI |     |Symbol|Capabilities?       |Datasets|Type|Figures|Decimals|
|----|-----|---|------|---|------|---|------|------|--------------------|--------|----|-------|--------|
|0   |COLOR|0  |10    |0  |100   |0  |10    |IDX   |\x00\x00\x00\x04\x84|1       |0   |2      |0       |
|1   |REFLT|0  |100   |0  |100   |0  |100   |PCT   |\x00\x00\x00\x04\x84|1       |0   |3      |0       |
|2   |AMBI |0  |100   |0  |100   |0  |100   |PCT   |\x00\x00\x00\x04\x84|1       |0   |3      |0       |
|3   |LIGHT|0  |100   |0  |100   |0  |100   |PCT   |\x00\x00\x00\x04\x84|3       |0   |3      |0       |
|4   |RREFL|0  |1024  |0  |100   |0  |1024  |RAW   |\x00\x00\x00\x04\x84|2       |1   |4      |0       |
|5   |RGB I|0  |1024  |0  |100   |0  |1024  |RAW   |\x00\x00\x00\x04\x84|4       |1   |4      |0       |
|6   |HSV  |0  |360   |0  |100   |0  |360   |RAW   |\x00\x00\x00\x04\x84|3       |1   |4      |0       |
|7   |SHSV |0  |360   |0  |100   |0  |360   |RAW   |\x00\x00\x00\x04\x84|4       |1   |4      |0       |
|8   |DEBUG|0  |65535 |0  |100   |0  |65535 |RAW   |\x00\x00\x00\x04\x84|4       |1   |4      |0       |
|9   |CALIB|0  |65535 |0  |100   |0  |65535 |RAW   |\x00\x00\x00\x04\x84|7       |1   |5      |0       |

``` python
hub.port.A.device.mode(3) # Necessary before next line
hub.port.A.device.mode(3, b''+chr(1*9)+chr(0*9)+chr(1*9))
```



## Force Sensor


## Boost Color Sensor


``` python
hub.port.A.device.mode(5) # Necessary before next line
hub.port.A.device.mode(5, b''+chr(a))
```

__Parameters:__ 

*  a in [3 (green),4 (blue),6 (red),10 (white)]


### Example

Connect BoostSensor two port A and cycle through the 4 colors.

``` python
from hub import port
import utime

BoostSensor=port.A.device

BoostSensor.mode(5)         # Set mode to RGB I

colors = [3, 5, 9, 10]      #3: Blue; 5: Green; 9: Red; 10: White

for c in colors:
    BoostSensor.mode(5,b''+chr(c))
    utime.sleep_ms(1000)
```

## WeDo distance sensor

## WeDo gyro