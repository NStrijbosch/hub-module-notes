from hub import port

SensorA = port.A.device

SensorA.mode(5)  # first set the correct mode before sending data
SensorA.mode(5,b''+chr(9)+chr(9)+chr(9)+chr(9))