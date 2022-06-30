# PlantGL Tutorial - Objects and 3D-Visualization

PlantGL is an open-source graphic toolkit for the creation, simulation and analysis of 3D virtual plants.

In this **tutorial**, we will :
* create a Sphere object from PlantGL
* display some PlantGL objects in 3D

## Introduction

We need some packages to make this tutorial work.


```python
import k3d
from openalea.plantgl.all import *
from oawidgets.plantgl import PlantGL
```

## Sphere Construction and Display

Let's build a Sphere object from PlantGL.


```python
s=Sphere(radius=2)
```

Now, we display it with the oawidgets.PlantGL function.


```python
PlantGL(s)
```


    UGxvdChhbnRpYWxpYXM9MywgYXhlcz1bJ3gnLCAneScsICd6J10sIGJhY2tncm91bmRfY29sb3I9MTY3NzcyMTUsIGNhbWVyYT1bNC41LCA0LjUsIDQuNSwgMC4wLCAwLjAsIDAuMCwgMS4wLCDigKY=
    


## More Objects and more Displays

Let's have a scene object in which we add a Sphere and a Box objects.


```python
scene = Scene()
scene.add(Sphere())
b = Box()
tbox = Translated((1,0,0), b)
scene.add(tbox)
```

Now we visualize the scene.


```python
PlantGL(scene)
```


    UGxvdChhbnRpYWxpYXM9MywgYXhlcz1bJ3gnLCAneScsICd6J10sIGJhY2tncm91bmRfY29sb3I9MTY3NzcyMTUsIGNhbWVyYT1bNC41LCA0LjUsIDQuNSwgMC4wLCAwLjAsIDAuMCwgMS4wLCDigKY=
    


## Have fun !

Let's import cool stuff !


```python
from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from random import randint
```

Let's define some functions.


```python
def color():
    return Material(ambient=Color3(randint(0,255), randint(0,255), randint(0,255)))

def buildSphere(n, rows=2):
    """Build n Spheres at different positions"""
    s = Sphere()
    scene = Scene()
    for i in range(n):
        si = Translated((2*(i%rows),2*(i//rows),0), s)
        scene.add(Shape(si, color()))
    return PlantGL(scene, group_by_color=True)
```


```python
interact(buildSphere, n=widgets.IntSlider(min=1, max=100, step=1, value=10))
```


    aW50ZXJhY3RpdmUoY2hpbGRyZW49KEludFNsaWRlcih2YWx1ZT0xMCwgZGVzY3JpcHRpb249dSduJywgbWluPTEpLCBJbnRTbGlkZXIodmFsdWU9MiwgZGVzY3JpcHRpb249dSdyb3dzJywgbWHigKY=
    





    <function __main__.buildSphere>


