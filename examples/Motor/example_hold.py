from hub import port
from utime import sleep_ms

MotorA = port.A.motor

MotorA.pwm(40)     # start motor
sleep_ms(1000)     # wait 1 second
MotorA.hold()      # actively hold position
sleep_ms(10000)    # wait 10 second active resistance should be noticable
MotorA.float()     # float motor