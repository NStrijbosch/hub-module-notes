
This documentation covers all my findings on the hub module of the SPIKE Prime and MINDSTORMS Robot Inventor hubs. This module is a lower level module as the given documented modules provided in the official SPIKE Prime and MINDSTORMS Robot Inventor apps. 

There are both advantages and disadvantages of using this module:

__Advantages:__

*  The motor commands do not block the remainder of your program, this can be useful when you want motors to run (almost) in parallel, or if you want to motors to track a trajectory
*  Exploit UART communication over the PU ports. This allows:  
   The use of third party TTL UART sensors  
   With the right cable, hub to hub communication.
*  Use BT_VCP and USB_VCP class to get more control over the communication between a computer and the hub
*  Use ALL PoweredUp Sensors and Motors, including all their functionality. It is even possible to use the Boost color sensor to control Power Function motors!
*  Receive RAW data measurements from the sensor, in some cases this increase the resolution significantly.
*  A wide variety of other functions that are not available in the standard python modules, among others:  
   Reboot the hub  
   Adjust the idle time before automatic shut down  
   Rotate the display 
   Realign the axis of the sensor readings to your model 
   ...


__Disadvantages:__

*  There is no official documentation. I cannot guarantee any of my findings are correct.
*  The behaviour of some functions, e.g., relative position, are not automatically reset at the start of a program. This can cause strange behaviour.
*  It is not recommended to use this module parallel to the standard modules. 
*  It does not cover all functionalities of the standard modules.  


I started this documentation for my personal use until official documentation is published. All commands are found by trial and error. This documentation is not complete and there are no guarantees on its correctness. I am highly interested if you have some additional insights into the hub module!

