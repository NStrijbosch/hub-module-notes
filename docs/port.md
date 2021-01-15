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

When in GPIO mode after a small delay the functions to control pin 5 and pin 6 appear. 

## direction()

`port.A.p5.direction(read_write)`  
`port.A.p6.direction(read_write)`

Set the direction of the pins, either write high or low values or read high low values.

__Parameters:__

* read_write [int](data_types.md#int): value 1: write; value 0: read

__Sample code:__ 

``` python
from hub import port

p5 = port.A.p5
p6 = port.A.p6

p5.direction(1) # write to pin 5
p6.direction(0) # read from pin 6
```
  
## value()

`port.A.p5.value(signal)`  
`port.A.p6.value(signal)`

Either read or write to the pin depending on its direction.

__Parameters:__

*  signal [int](data_types.md#int): 1 (High) or 0(Low) if direction is write (1)
*  None: if direction is read

__Returns:__

*   [int](data_types.md#int): : 1 (High) or 0(Low) if direction is read (0)

__Sample code:__

``` python
from hub import port
from utime import sleep_ms

port.A.mode(3) #set GPIO mode

sleep_ms(1000) #small delay to wait for GPIO methods to appear

p5 = port.A.p5
p6 = port.A.p6

p5.direction(1) # write to pin 5
p6.direction(0) # read from pin 6

p5.value(1)# set pin 5 to high

print("Signal on pin 6: " + str(p6.value()))
```

```
>>> Signal on pin 6: 1
```






