from hub import port

MotorA = port.A.motor

# Set mode to absolute position
MotorA.mode(3)
curr_abs_pos, = MotorA.get()

MotorA.preset(curr_abs_pos)