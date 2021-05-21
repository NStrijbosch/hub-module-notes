from hub import port

MotorA = port.A.motor
MotorB = port.B.motor

Pair=MotorA.pair(MotorB)

Pair.run_for_degrees(270, 100, 50) # Motor A turns 360 and Motor B turns 180
                                   # Combined distance = 2*270