
## volume()

set volume of on hub speaker

```
hub.sound.volume(volume)
```

__Parameters:__

*  volume (integer): 0-10

## beep()

play a beep with on hub speaker

```
hub.sound.beep(freq,time,waveform)
```

__Parameters:__

*  freq: float in range 0.0-?
*  time: ms (integer)
*  waveform: 0:sin, 1:square, 2:triangle, 3:sawtooth

## play()

probably play a music file

```
hub.sound.play(music_file?)
```

__Parameters:__

*  music_file? which format?