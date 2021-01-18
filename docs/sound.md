

## beep()

`sound.beep(freq,time,waveform)`

play a beep with on hub speaker

__Parameters:__

*  freq [float](data_types.md#float): frequency in Hz
*  time [int](data_types.md#int): time in milliseconds
*  waveform [int](data_types.md#int):  
    SOUND_SIN=0  
    SOUND_SQUARE=1  
    SOUND_TRIANGLE=2  
    SOUND_SAWTOOTH=3  

__Sample code:__

``` python
from hub import sound

sound.beep(10,1000,0)
```

## volume()

`sound.volume()`

Set volume of on hub speaker.

__Parameters:__

*  volume [int](data_types.md#int): volume in range 0-10

__Sample code:__

``` python
from hub import sound
from utime import sleep_ms

sound.volume(10)
sound.beep(20,1000,0)

sleep_ms(1000) # wait for previous beep to end

sound.volume(3)
sound.beep(20,1000,0)
```


## play() 

`sound.play()`

!!! todo
    Not sufficiently tested. Check [nutki's spike-tools](https://github.com/nutki/spike-tools) for music file converter. 