class Led:
    """
    Class to control build in LED
    """
    

class Button:
    """ Class to control a button """

    def __init__(self):
        """ Create a instance of a single button """

    def is_pressed(self):
        """
        check if button is pressed

        :returns: True if button is pressed; False if button is not pressed
        """

    def was_pressed(self):
        """
        check if button was pressed since last call 

        :returns: True if button was pressed since last call; False if button was not pressed since last call
        """

    def presses(self):
        """
        Number of presses since last call

        :returns: integer value of number of presses since last call
        """          

class Motion:
    """ Class to handle motion sensor in PoweredUP hub

    Supported on: |technic_hub|
    """

    def accelerometer(self):
        """ Measure acceleration around three axis 

        :return: accleration around x,y,z axis
        :rtype: tuple
        """

    def gyroscope(self):
        """ Measure gyro rates around three axis 

        :returns: gyro rates around x,y,z axis
        :rtype: tuple
        """

    def yaw_pitch_roll(self):
        """ Measure yaw pitch roll angles  

        :return: yaw pitch roll angle
        :rtype: tuple
        """
        
class A():
    """ Class to control a PoweredUp device connect to a single port """
    
            
class Port():
    """ Class to control PoweredUp devices connected to the physical ports """   
   
    
class Device:
    """ The Device class is a sub class of the ``port`` class which allows to control PoweredUP Sensors. It can be used via ``sensor=hub.port.A.device``."""
    
    def mode(self, mode, *data):
        """ Set the mode of the sensor

        :param mode: new mode
        :type mode: byte
        
        :param *data: optional data to be send allong with mode, e.g., to turn on LEDs of a sensor
        :type *data: bytearray

        .. literalinclude:: ../../examples/Device/example_mode.py
        .. literalinclude:: ../../examples/Device/example_mode_data.py
        """

    def get(self):
        """ Get measurement of the sensor corresponding to the active mode

        :returns: measurement
        :rtype: tuple

        .. literalinclude:: ../../examples/Device/example_get.py
        """
    
class Motor:
    """ The Motor class is a sub class of the ``port`` class which allows to control PoweredUP Motors. It can be used via ``sensor=hub.port.A.motor``."""

    def default(pid=(0, 0, 0), max_power=0, speed=0, stall=True, acceleration=100, deceleration=150, stop=1, callback=None):
        """ Set default parameters of the motor 

        :param pid: PID controller gains
        :type pid: tuple

        :param max_power: maximum power that can be used by motor
        :type max_power: integer

        :param speed: default speed
        :type speed: integer

        :param stall: set stall detection on or off
        :type stall: boolean

        :param acceleration: the duration time for an acceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an acceleration time of 300 ms from 40% to 70%
        :type acceleration: int
        
        :param deceleration: the duration time for a deceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an deceleration time of 300 ms from 70% to 40%
        :type deceleration: int

        :param stop: action performed after the given time: ``float = 0``, ``brake = 1``, ``hold = 2``
        :type stop: int

        :param callback: set callback that is called at (?)
        :type callback: bound method

        :returns: list of current default motor settings
        :rtype: dict
        
        .. literalinclude:: ../../examples/Motor/example_default.py
        """

    def mode(self, mode):
        """ Set the mode of the motor, this mainly affects the measurement output

        :param mode: new mode
        :type mode: int

        .. literalinclude:: ../../examples/Motor/example_mode.py
        """

    def preset(self,angle):
        """ Preset the value of the relative position

        :param angle: preset position: best practice is to use current position, or absolute position
        :type angle: int

        .. literalinclude:: ../../examples/Motor/example_preset.py
        """

    def pid(self, p, i, d):
        """ Set controller gains of the PID controller

        .. warning::
            The applied values of the actual controller do not seem to change.

        :param p: proportional gain
        :type p: int
        :param i: integral gain
        :type i: int
        :param d: derivative gain
        :type d: int

        .. literalinclude:: ../../examples/Motor/example_pid.py
        """

    def get(self):
        """ Get measurement of the motor corresponding to the active mode

        :returns: measurement
        :rtype: tuple

        .. literalinclude:: ../../examples/Motor/example_get.py
        """

    def busy(self, busy_type):
        """ Check if motor is busy with performing an action

        :param busy_type: type of action: 0 (? yet unknown action); 1 reaching a target
        :type busy_type: int

        .. literalinclude:: ../../examples/Motor/example_busy.py
        """

    def pwm(self,power):
        """ Set motor power

        :param power: in range [-100,..., 100]
        :type power: int

        .. literalinclude:: ../../examples/Motor/example_pwm.py
        """

    def run_at_speed(self,speed, max_power=100, acceleration=100, deceleration=100):
        """ Start motor at given speed

        :param speed: a percentage off the maximum speed of the motor in the range [-100,..., 100] 
        :type speed: int
        
        :param max_power: maximum power that can be used by the motor
        :type max_power: int
        
        :param acceleration: the duration time for an acceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an acceleration time of 300 ms from 40% to 70%
        :type acceleration: int
        
        :param deceleration: the duration time for a deceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an deceleration time of 300 ms from 70% to 40%
        :type deceleration: int

        .. literalinclude:: ../../examples/Motor/example_run_at_speed.py
        """

    def run_for_time(self,time, speed=50, max_power=100, acceleration=100, deceleration=100, stop_action=0):
        """ Rotate motor for a given time

        :param time: time in milliseconds
        :type speed: int

        :param speed: a percentage off the maximum speed of the motor in the range [-100,..., 100] 
        :type speed: int
        
        :param max_power: maximum power that can be used by the motor
        :type max_power: int
        
        :param acceleration: the duration time for an acceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an acceleration time of 300 ms from 40% to 70%
        :type acceleration: int
        
        :param deceleration: the duration time for a deceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an deceleration time of 300 ms from 70% to 40%
        :type deceleration: int
        
        :param stop_action: action performed after the given time: ``float = 0``, ``brake = 1``, ``hold = 2``
        :type stop_action: int

        .. literalinclude:: ../../examples/Motor/example_run_for_time.py
        """
        
    def run_for_degrees(self,degrees, speed=50, max_power=100, acceleration=100, deceleration=100, stop_action=0):
        """ Rotate motor for a given number of degrees relative to current position

        :param degrees: relative degrees
        :type degress: int

        :param speed: a percentage off the maximum speed of the motor in the range [-100,..., 100] 
        :type speed: int
        
        :param max_power: maximum power that can be used by the motor
        :type max_power: int
        
        :param acceleration: the duration time for an acceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an acceleration time of 300 ms from 40% to 70%
        :type acceleration: int
        
        :param deceleration: the duration time for a deceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an deceleration time of 300 ms from 70% to 40%
        :type deceleration: int
        
        :param stop_action: action performed after the given time: ``float = 0``, ``brake = 1``, ``hold = 2``
        :type stop_action: int

        .. literalinclude:: ../../examples/Motor/example_run_for_degrees.py
        """

    def run_to_position(self,degrees, speed=50, max_power=100, acceleration=100, deceleration=100, stop_action=0):
        """ Rotate motor for a given number of degrees relative to current position

        :param degrees: relative degrees
        :type degress: int

        :param speed: a percentage off the maximum speed of the motor in the range [-100,..., 100] 
        :type speed: int
        
        :param max_power: maximum power that can be used by the motor
        :type max_power: int
        
        :param acceleration: the duration time for an acceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an acceleration time of 300 ms from 40% to 70%
        :type acceleration: int
        
        :param deceleration: the duration time for a deceleration from 0 to 100%. i.e. a time set to 1000 ms. should give an deceleration time of 300 ms from 70% to 40%
        :type deceleration: int
        
        :param stop_action: action performed after the given time: ``float = 0``, ``brake = 1``, ``hold = 2``
        :type stop_action: int

        .. literalinclude:: ../../examples/Motor/example_run_to_position.py
        """

    def float(self):
        """ Float motor from current position 
        
        .. literalinclude:: ../../examples/Motor/example_float.py
        """

    def brake(self):
        """ Brake motor at current position 
        
        .. literalinclude:: ../../examples/Motor/example_brake.py
        """

    def hold(self):
        """ Actively hold motor at current position 
        
        .. literalinclude:: ../../examples/Motor/example_hold.py
        """

    def pair(self, motor):
        """ Pair two motors. Both motors can now be controlled as a pair (even with different speeds).

        :param motor: motor to pair current motor with
        :type motor: Motor

        .. literalinclude:: ../../examples/Motor/example_pair.py
        """
