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

Below you find a list of all available PU sensors with a table that shows their available modes. Moreover, it is possible to send data to some sensor, sample codes are given to demonstrate this. 

## Ultrasonic Sensor

__Available modes:__

|Mode|Name |RAW          |PCT        |SI           |Symbol|Capabilities?       |Datasets|Type|Figures|Decimals|
|----|-----|-------------|-----------|-------------|------|--------------------|--------|----|-------|--------|
|0   |DISTL(distance long)|0.0...2500.0 |0.0...100.0|0.0...250.0  |cm    |\x00\x00\x00\x04\x84|1       |1   |5      |1       |
|1   |DISTS(distance short)|0.0...320.0  |0.0...100.0|0.0...32.0   |cm    |\x00\x00\x00\x04\x84|1       |1   |4      |1       |
|2   |SINGL(distance)|0.0...2500.0 |0.0...100.0|0.0...250.0  |cm    |\x00\x00\x00\x04\x84|1       |1   |5      |1       |
|3   |LISTN(?)|0.0...1.0    |0.0...100.0|0.0...1.0    |ST    |\x00\x00\x00\x04\x84|1       |0   |1      |0       |
|4   |TRAW (time?)|0.0...14577.0|0.0...100.0|0.0...14577.0|us    |\x00\x00\x00\x04\x84|1       |2   |5      |0       |
|5   |LIGHT(led lights)|0.0...100.0  |0.0...100.0|0.0...100.0  |pct   |\x00\x00\x04\x84    |4       |0   |3      |0       |
|6   |PING(digital read?)|0.0...1.0    |0.0...100.0|0.0...1.0    |pct   |\x80\x00\x00\x04\x84|1       |0   |1      |0       |
|7   |ADRAW(Analog on Pin 5/6 to Digital?)|0.0...1024.0 |0.0...100.0|0.0...1024.0 |pct   |\x80\x00\x00\x04\x84|1       |1   |4      |0       |
|8   |CALIB|0.0...255.0  |0.0...100.0|0.0...255.0  |pct   |\x00\x00\x04\x84    |7       |0   |3      |0       |

### Sending data to leds

All four leds of the ultrasonic sensor can be controlled individually, see [mode](#mode) for details on how to send data. 

__Sample code:__

``` python
from hub import port

USsensor = port.A.device

USSensor.mode(5)  # set mode to light

led1 = 9  #brightness in range 0...9
led2 = 0  #brightness in range 0...9
led3 = 9  #brightness in range 0...9
led4 = 0  #brightness in range 0...9
USSensor.mode(5,b''+chr(led1)+chr(led2)+chr(led3)+chr(led4))
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

### Sending data to leds

All three leds of the color sensor can be controlled individually, see [mode](#mode) for details on how to send data to activate them. 

__Sample code:__

``` python
from hub import port

COLORsensor = port.A.device

COLORSensor.mode(3)  # set mode to light

led1 = 9  #brightness in range 0...9
led2 = 0  #brightness in range 0...9
led3 = 9  #brightness in range 0...9

COLORSensor.mode(3,b''+chr(led1)+chr(led2)+chr(led3))
```

## Force Sensor


## Boost Color Sensor



### Setting the color of the led

Led of the boost sensor can be controlled, see [mode](#mode) for details on how to send data to activate it. 

__Sample code:__

``` python
from hub import port
from utime import sleep_ms

BoostSensor=port.A.device

BoostSensor.mode(5)         # Set mode to RGB I

colors = [3, 5, 9, 10]      #3: Blue; 5: Green; 9: Red; 10: White

for c in colors:
    BoostSensor.mode(5,b''+chr(c))
    sleep_ms(1000)
```

### Sending IR signals to PF receiver

The BoostSensor is capable of sending IR data, see [mode](#mode) for details on how to send data. 

``` python
from hub import port
from utime import sleep_ms

BoostSensor=port.A.device

BoostSensor.mode(7)         # Set mode IR

BoostSensor.mode(7, b'' + chr(247) + chr(255))  # channel 4 
BoostSensor.mode(7, b'' + chr(3) + chr(14))     # channel 3 motor red

### Two bytes seem necessary
### Observed behaviour is for now really inconsistent, given that I am sending random bytes
### A member from the community is working on a library (hopefully published soon!)
```

## WeDo distance sensor

|Mode|Name       |RAW|      |PCT|      |SI |      |Symbol|Capabilities?           |Datasets|Type|Figures|Decimals|
|----|-----------|---|------|---|------|---|------|------|------------------------|--------|----|-------|--------|
|0   |LPF2-DETECT|0  |10    |0  |100   |0  |10    |      |\x10\x00\x00\x00\x00\x00|1       |0   |3      |0       |
|1   |LPF2-COUNT |0  |100   |0  |100   |0  |100   |CNT   |\x10\x00\x00\x00\x00\x00|1       |2   |4      |0       |
|2   |LPF2-CAL   |0  |1023  |0  |100   |0  |1023  |RAW   |\x10\x00\x00\x00\x00\x00|3       |1   |3      |0       |

## WeDo gyro