from hub import port

MotorA = port.A.motor

MotorA.mode(2)# set mode to absolute position

MotorA.preset(MotorA.get()[0])# preset 0 position to absolute zero position

# Turn motors to different positions in parallel
MotorA.run_to_position(180,speed=50)