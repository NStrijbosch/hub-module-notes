from hub import port

MotorA = port.A.motor

MotorA.mode(3)          # Absolute position mode
abs_pos = MotorA.get()[0]
print("Absolute position: " + str(abs_pos))

Motor.mode([(1, 0), (2, 2)])  #Speed in RAW units and relative position in SI units
measurements = MotorA.get()
print("Speed : " + str(measurements[0]) + " Relative position: " + str(measurements[1]))