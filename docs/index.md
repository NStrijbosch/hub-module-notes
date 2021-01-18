This documentation covers all my findings on the hub module of the SPIKE Prime and MINDSTORMS Robot Inventor hubs. This module is a lower level module as the given documented modules provided in the official SPIKE Prime and MINDSTORMS Robot Inventor apps.

Use the menu to explore all functions available in the hub module!

---

There are both advantages and disadvantages of using this module:

__Advantages:__

<ul class='index_list'>
   <li>The motor commands do not block the remainder of your program, this can be useful when you want motors to run (almost) in parallel, or if you want motors to track a trajectory
   </li>
   <li> Use UART communication over the PU ports. This allows for:
      <ul  class="index_list">
         <li>
         third party TTL UART sensors via the Ultrasonic sensor's breakout.  
         </li>
         <li>
          hub to hub communication  (with the right cable)
         </li>
      </ul>
   </li>
   <li>
      Use BT_VCP and USB_VCP class to get more control over the communication between a computer and the hub  
   </li>
   <li>
      Use ALL PoweredUp Sensors and Motors, including all their functionality. It is even possible to use the Boost color sensor to control Power Function motors!
   </li>
   <li>
      Receive RAW data measurements from the sensor, in some cases this increase the resolution significantly. 
   </li>
   <li>
      A wide variety of other functions that are not available in the standard python modules, among others: 
      <ul class="index_list">
         <li>
          Reboot the hub  
         </li>
         <li>
            Adjust the idle time before automatic shut down  
         </li>
         <li>
            Rotate the display 
         </li>
         <li>
            Realign the axis of the sensor readings to your model 
         </li>
         <li>
            ....
         </li>
      </ul>
   </li>
</ul>

__Disadvantages:__

<ul class="index_list">
   <li>
      There is no official documentation. I cannot guarantee any of my findings are correct. 
   </li>
   <li>
      The behaviour of some functions, e.g., relative position, are not automatically reset at the start of a program. This can cause strange behaviour.
   </li>
   <li>
      It is not recommended to use this module parallel to the standard modules. This sometimes causes strange behaviour.
   </li>
</ul>

---

I started this documentation for my personal use until official documentation is published. All commands are found by trial and error. This documentation is not complete and there are no guarantees on its correctness. I am highly interested if you have some additional insights into the hub module!

--- 


© Nard Strijbosch {{ date }}

<sub>LEGO® is a trademarks of The LEGO Group of companies which does not sponsor, authorize or endorse this site.  The LEGO Group is not liable for any loss, injury or damage arising from the use or misuse of these codes.</sub>

