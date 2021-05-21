from hub import port

SensorA = port.A.device

SensorA.mode(1)            # Set sensor to mode 3

print("Mode sensor port A: " + str(SensorA.mode()))