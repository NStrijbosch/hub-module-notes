In the hub module, two virtual com port (VCP) classes are available: `BT_VCP` and `USB_VCP`. Both work identically. This class will be useful when you want to communicate over USB or Bluetooth with a computer which is performing, computationally heavy calculations, and you only want the hub to perform motor/sensor actions. In the remainder all example use BT_VCP but everything will work similarly using USB_VCP. 

!!! todo
    The VCP classes can make use of buffer object. More tests are necessary to get fully document these options.

# REPL or VCP

Using the Read Eval Print Loop (REPL) you can send whatever command you like to the hub and it will directly execute them. Using this it is possible to have script running on a PC with, e.g., computationally heavy calculations, and only send motor and sensor commands to the hub. The advantage of the REPL is that is running by default. 

The advantage of using BT_VCP or USB_VCP is that a script is running on the hub and you control at specific moments in the script at which point you want to have communication with the computer. This way the computer does not have to send all motor commands but, e.g., only a short message which triggers sequence of motor commands on the hub. 

# VCP

## VCP()

`BT_VCP(port)`

Setup a new VCP object. 

__Parameters:__

*  port [int](data_types.md#int): the bluetooth port to use as VCP.


__Sample code:__

``` python
from hub import BT_VCP

com = USB_VCP(0)
```

## recv()

`BT_VCP.recv(data,timeout)`

Receive data over the VCP

__Parameters:__

*  data [int](data_types.md#int): number of bytes
*  timeout [int](data_types.md#int): number of milliseconds the VCP waits on data

__Sample code:__

``` python
from hub import BT_VCP

com = BT_VCP(0)

message = com.recv(4,1000)

message.decode('UTF-8')

print('Received message: ' + message)
```

<span class='shell_output'>
\> Received message: test
</span>

## readline()

`BT_VCP.readline()`

Read a whole line from the VCP

__Sample code:__

``` python
from hub import BT_VCP

com = BT_VCP(0)

message = com.readline()

message.decode('UTF-8')

print('Received message: ' + message)
```

<span class='shell_output'>
\>Received message: test
</span>

## readlines()

`BT_VCP.readlines()`

Read as much lines from the VCP as possible

__Sample code:__

``` python
from hub import BT_VCP

com = BT_VCP(0)

message = com.readlines()

message.decode('UTF-8')

print('Received message: ' + message)
```

<span class='shell_output'>
\> Received message: test</br>
\> test</br>
\> test<br/>
\> test
</span>

## write()

`BT_VCP.write(message)`

write a message over the VCP

__Parameters:__

*  message [str](data_types.md#str) (buffer also possible?): message to send

__Sample code:__

``` python
from hub import BT_VCP

com = BT_VCP(0)

message = com.write("Test from hub")
```









