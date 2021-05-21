from hub import port

MotorA = port.A.motor
MotorB = port.B.motor

# Turn motors to different positions in parallel
MotorA.run_for_degrees(100,speed=50)
MotorB.run_for_degrees(-400,speed=50)