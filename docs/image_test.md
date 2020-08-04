# Image

constructing images that can be displayed using:
```
hub.display.show(image)
```


```
image = hub.Image("90009:"
                        "09090:"
                        "00900:"
                        "09090:"
                        "90009")    
```

```
image = hub.Image("90009\n09090\n00900\n09090\n90009"
```

```
 image = hub.Image(2, 2, b'\x08\x08\x08\x08')
```

```
hub.Image.set_pixel(3,1,6) 
``` 
Only works for custom images

```
hub.Image.width()
hub.Image.height()
hub.Image.get_pixel(x,y)
```