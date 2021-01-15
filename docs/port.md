The port class controls everything that is connected to the PU connectors on the hub. The main two sub classes are [device](sensors.md) to use sensors and [motor](motors.md) to control motors. 

# Port modes

## mode

`port.A.mode(mode)`

> The modes can be devided in three categories:  
> *  Default: for PU sensors and PU motors use [device](sensors.md) to use sensors and [motor](motors.md)
> *  Duplex (both full and half): communicate via UART protocol. For details see [mode Duplex](#port-mode-duplex).
> *  GPIO: set pin 5 and 6 to high/low. For details see [mode GPIO](#port-mode-GPIO).

__Parameters:__

*  mode [int](data_types.md#int): value could be  
    MODE_DEFAULT = 0
    MODE_FULL_DUPLEX = 1
    MODE_HALF_DUPLEX = 2
    MODE_GPIO = 3

__Sample code:__

```python
from hub import port

port.A.mode(1) ## set full duplex mode
```

# Port mode Duplex

When in FULL/HALF duplex mode after a small delay standard UART methods appear. Unfortunately, buffer specific methods are not available. 

## baud()

`port.A.baud(baud_rate)`

Set baud rate. 

__Parameters:__

* baud_rate [int](data_types.md#int)

__Sample code:__

``` python
from hub import port
from utime import sleep_ms

portA = port.A

portA.mode(1)   # set full duplex mode 
sleep_ms(1000)  # wait for all duplex methods to appear

portA.baud(115200) # set baud rate

```

## read()

`read(nbytes)`

read a number of bytes from the UART buffer. 

__Parameters:__

*  nchars [int](data_types.md#int): number of bytes to read

__Returns:__

* [bytearray](data_types.md#bytearray)

__Sample code:__

``` python
from hub import port
from utime import sleep_ms

portA = port.A

portA.mode(1)   # set full duplex mode 
sleep_ms(1000)  # wait for all duplex methods to appear

portA.baud(115200) # set baud rate

data=portA.read(4)

print('data received: ' + str(data.decode('UTF-8')))
```

```
data received: test
```

## write

`write(data)`

__Parameters:__

* data ([str](data_types.md#string))

__Sample code:__

``` python
from hub import port
from utime import sleep_ms

portA = port.A

portA.mode(1)   # set full duplex mode 
sleep_ms(1000)  # wait for all duplex methods to appear

portA.baud(115200) # set baud rate

data=portA.write('test')
```

# Port mode GPIO

