from hub import port

ForceSensor = port.A.device

ForceSensor.mode(4)        # Force in RAW units
force = ForceSensor.get()[0]
print("force: " + str(force))