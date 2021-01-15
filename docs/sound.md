

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

hub.sound.beep(1,1000,0)
```

## volume()

`sound.volume()`

Set volume of on hub speaker.

__Parameters:__

*  volume [int](data_types.md#int): volume in range 0-10

__Sample code:__

``` python
from hub import sound

hub.sound.volume(3)
hub.sound.beep(1,1000,0)
hub.sound.volume(10)
hub.sound.beep(1,1000,0)
```


## play() TODO

`sound.play()`

probably play a music file (what format?)

__Parameters:__

*  music_file? which format?