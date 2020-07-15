
# Sensors

## Commands

### Set Mode
All of the sensors have a few different operating modes. Details about the modes for each specific sensor can be found below. 

The operation mode of the sensor can be changed using the following command
```
hub.port.A.device.mode(mode)
```

### Read values


```
hub.port.A.device.get(unit)
```
These are the values obtained when using the scratch programming environment

In RAW units
```
hub.port.A.device.get(hub.port.A.FORMAT_RAW)
``` 

this can significantly improve the resolution

In Percent
```
hub.port.A.device.get(hub.port.A.FORMAT_PCT)
```

In SI units
```
hub.port.A.device.get(hub.port.A.FORMAT_SI)
```

### Ultrasonic Sensor
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


### Color Sensor

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



### Force Sensor

[a relative link](test_link.md)
