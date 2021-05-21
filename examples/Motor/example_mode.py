from hub import port

MotorA = port.A.motor

MotorA.mode(3)              # Set motor mode to absolute position
MotorA.mode([3,2])          # Set motor mode to absolute position and relative position

print("Mode motor port A: " + str(MotorA.mode()))