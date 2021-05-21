from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.run_for_time(1000,speed=50)   # turn motor for 1000 milliseconds at speed 50