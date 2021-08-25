!!! info The latest version of the MINDSTORMS App (10.2.0) includes a word block extension that allows for hub2hub communication. I recommend using this extension over this library. 

!!! info The latest version of the SPIKE app (2.0.0) includes a firmware update for the hub that breaks the current version of the `hub2hub` library. A fix to this issue is coming soon. 


# hub2hub
The `hub2hub` library is not part of the original firmware of either the Robot Inventor hub or the SPIKE Prime hub. In the official SPIKE Prime firmware, a low-level `ubluetooth` library is available to be able to directly communicate between hubs. The documentation of this module can be found here: [ubluetooth documentation](https://docs.micropython.org/en/latest/library/ubluetooth.html). 

The main goal of the `hub2hub` library is to simplify the python code required to setup and maintain a BLE connection between hubs in contrast to the low-level `ubluetooth` library available in the official firmware. Installation of the library and writing programs that use it are both possible via the official LEGO Education SPIKE Prime app, as explained below.

# Installation

The following steps guide you through the process to install the `hub2hub` library. These steps should be repeated for each of the hubs that will be used in the BLE network. 

### Step 1:

If you did not update your SPIKE Prime software yet, install one of the latest versions of the SPIKE Prime app (1.3.4 or 1.3.3) and connect your device. If the app asks for a hub update, perform the hub update.

!!! Warning
    This library does not work when using the MINDSTORMS Robot Inventor app. Due to a firmware difference, the Bluetooth module is not available when using the MINDSTORMS Robot Inventor App and corresponding firmware. Luckily you can just connect your MINDSTORMS hub to the SPIKE Prime app and update the SPIKE PRIME Firmware on the hub.

### Step 2:

Download and open the project: [Install_hub2hub_v003.llsp](https://github.com/NStrijbosch/hub2hub/blob/main/install/Install_hub2hub_v003.llsp?raw=true). 

### Step 3:

Set the SPIKE Prime execution mode in download mode, and select an unused project slot. 

![download](../figures/download.PNG)

### Step 4:

Run the project by pressing the play button and wait until the hub is powered down. (if you use a USB cable to connect the hub, the hub will probably restart automatically)

![play](../figures/run.PNG)

### Step 5:

Installation is successful. The hub2hub library is now installed on your hub. You can now safely use the slot you used for this installation for a new project. 

!!! warning
    Firmware updates of the hub are likely to remove the library from the filesystem of the hub. Hence, this procedure should be repeated if a firmware update removed the library from the hub. 

### Step 6: (optional)

To test if the library is functioning properly try the example projects: [parent_example.llsp](https://github.com/NStrijbosch/hub2hub/blob/main/examples/parent_example.llsp?raw=true) and [child_example.llsp](https://github.com/NStrijbosch/hub2hub/blob/main/examples/child_example.llsp?raw=true) on two seperate hubs. 

# Disclaimer

This library is still actively developed. There are still some known issues:

<ul class='index_list'>
 <li>The hubs do not automatically disconnect when a program is stopped. To disconnect the hubs you need to restart the hubs. In other words: after each time you run the project restart the hubs before you run the program again</li>
 <li>It might take a few tries to get a hub connected to a large BLE network.</li>
</ul>

If you run in any additional issues you can report them [here](https://github.com/NStrijbosch/hub2hub/issues).

# BLE Networks and Routing

Before introducing the commands from the hub2hub library first some background information on the communication protocol used by the hub2hub library is required. 

In a typical BLE network there exist one parent device and one or more child devices. This parent device can send a request to all child devices in the network. An example of a request could be: __Set left motor speed to 50__. After sending this request the parent will wait on a response from the child device if the message was successfully received. The child device could respond with for example __motor speed set to 50__. After this, the parent can send a new request to the same hub or any other hub. This protocol ensures only one hub is sending messages, thereby not overloading the BLE network with messages. This protocol also allows for bidirectional communication, since the child hub can respond with any message to the root, with the only limitation that the root always has to send a request first. 

The MINDSTORMS Robot Inventor and SPIKE Prime hubs are only able to connect to 3 child devices and 1 parent device. For different projects with different numbers of hubs, this will lead to different BLE network structures. Below the star network topology is explained for connecting up to 4 hubs. An extension of this network is the Tree network which does not limit the number of hubs connected to the parent. (At the moment the Tree network structure is still in an experimental phase, the reliability of connections in this type of networks is not at the desired level yet)

### Star network

In a star network there is one parent hub and a maximum of three child hubs, with an address as given in the Figure below. 

![Star Network](../figures/star_network.png)

### Tree network

The tree network is an extension of the star network. In this network structure, the child hubs can act as both a child and as a parent hub to three other child hubs. See the figures below for example networks. 

__Example of a tree network with one intermediate level:__

![Tree Network](../figures/tree_network_01.png)

__Example of a tree network with two intermediate levels:__

![Tree Network](../figures/tree_network_02.png)

This network can be viewed as a family tree, where the oldest grandfather (root parent) can send requests to his complete offspring. Requests to a child not directly connected to the root parent will be routed to the child, via the parents in the intermediate levels. Similarly, the response of the child is routed via the same path. 

In a tree network different levels can be distinguished:

<ul class='index_list'>
 <li>Level 0: one root parent, this is the parent that can send request to all other child hubs. </li>
<li>Level 1, ..., N-1 intermediate levels: the hubs are both a child and a parent or only a child</li>
<li>Level N: The highest level where the hubs are only a child</li>
</ul>
The addresses of the hubs follow the following rules:

<ul class='index_list'>
* Level 0: 000.., the number of zeros is the number of layers except the root layer
<li>Level 1: 100..., 200..., or 300...</li>
<li>Level 2: the child hubs connected to one of the hubs from Level 1: copy the first digit of the parent hub, and add 1, 2, or 3 behind this one. For the hubs connected to the hub with address 100..., its child hub addressess are 110..., 120..., and 130.... </li>
<li>Level 3: similarly to level 2 copy the first 2 digits of the parent and add 1, 2, or 3. 
</li>
</ul>

# hub2hub 

## Setup the BLE network

### import hub2hub

The only thing necessary from the hub2hub library is the BLEnetwork, this can be imported using

__Example code:__

``` python
from hub2hub import BLEnetwork
```

### Define network

A network can be defined as a dictionary with key value pairs representing the name of the hub (string) as key and its address in the network (string) as the value. 

__Example code:__

``` python
network = { 
## Name: Address 
    'A': '0',  
    'B': '1',  
    'C': '2',  
    'D': '3',  
}
```

### BLEnetwork()

`BLEnetwork(name, network, state=initial_state)`

Initiate the hub as part of the BLE network. 

__Parameters:__

*  name (str): name of this hub in the BLE network
*  network (dict): the BLE network this hub operates in
*  state (optional): the state value can be of any type, and represents a variable that can be changed anywhere, including the `on_request`and `on_response` methods, in the program using `ble.state`.  

__Sample code:__

``` python
from hub2hub import BLEnetwork

network = { 
## Name: Address 
    'A': '0',  
    'B': '1',  
    'C': '2',  
    'D': '3',  
}

ble = BLEnetwork('A', network, state=0)
```

### connect()

`connect()`

Establish connection with the BLE network. First the children are connected, afterwards the parent is connected. 

__Sample code:__

``` python
ble.connect()
```

### is_connected()

`is_connected()`

__Returns:__

*  bool: `True` if all children and parent are connected; `False` if one of the children or parent is not connected. 

__Example code:__

``` python
while ble.is_connected():
    print('connected to the BLE network')
    sleep_ms(100)
```

## Root methods

Next the methods that can be used by the root parent are introduced

### request_child

`request_child(child,message,wait_for_response=True)`

Send a request to a child in the network

__Parameters:__

*  message: the message that is send along with the request. The value can be of any type. 
*  child: name of the child to which the request is send
*  wait_for_response: `True` if you expect a response message from the child, the parent cannot send new messages untill it received the response; `False` if the child will not respond with a message after receiving the request, the parent can send a new message directly.


__Sample code:__

``` python
### from the example project: parent.llsp (step 6 of installation instructions)

# Create message based on button presses
message = 0
if buttonL.was_pressed():
    message -=1
if buttonR.was_pressed():
    message +=1

# Send request to child B
ble.request_child('B', message, wait_for_response=True)
```

### set_on_response()

`set_on_response(callback)`

Set the function that will be executed when a response from a child is received. 

__Parameters:__ 

*  Callback: a user defined function with the arguments: message, and the child from which the reponse originates. 

__Sample code:__

``` python
### on_response from the example project: parent.llsp (step 6 of installation instructions)
def on_response(message,child):
    # if response is from child 'B'
    if child is 'B':
        # update BLE state
        ble.state = (ble.state + message) % 12
        # update Display
        display.show(Image.ALL_CLOCKS[ble.state])

    return

ble.set_on_response(on_response)
```

## Child methods

Next the methods that can be used by all children are introduced

### set_on_request()

`set_on_request()`

set the function that will be executed when a request from the root is received by a child. 

__Parameters:__

*  callback function: this function will be executed if a request is received from the root. The parameters of this function is the message send by the parent. The callback can return a message to the parent or `None` (Returning `None` is only adviced if the parent does not require a response).

__Sample code:__

``` python
### on_request from the example project: child.llsp (step 6 of installation instructions)
def on_request(message):

    # update BLE state
    ble.state = (ble.state + message) % 12

    # Update display
    display.show(Image.ALL_CLOCKS[ble.state])

    # Define response message
    response_message = 0
    if buttonL.was_pressed():
        response_message -=1
    if buttonR.was_pressed():
        response_message +=1

    # respond with response_message
    return response_message

ble.set_on_request(on_request)
```

!!! note
    It is important to keep the execution time of the on_request function as short as possible. The response message to the root parent will be send after completion of the callback. Hence, during the execution of this method no other messages can be send in the BLE network.
