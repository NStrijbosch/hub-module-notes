from hub import port

MotorA = port.A.motor

MotorA.default(max_power = 50, stop = 2) #set max power to 50 and stop action to hold
print("default settings: " + str(MotorA.default()))