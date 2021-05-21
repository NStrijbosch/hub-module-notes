from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.run_at_speed(speed=50)   # turn motor at speed 50
sleep_ms(1000)                  # wait 1000 millisecond
MotorA.run_at_speed(0)          # turn motor at speed 0, i.e., stop