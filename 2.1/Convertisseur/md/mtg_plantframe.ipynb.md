# MTG Tutorial - PlantFrame

[PlantFrame](https://mtg.readthedocs.io/en/latest/user/tutorial_plantframe.html) is a method to compute the geometry of each organ of a Plant Architecture. Geoemtrical data is associated to some vertices of the architecture (aka MTG). But often, geometrical information is missing on some vertex. Constraints have to be solved to compute missing values.

The stages of the **PlantFrame** are:
* insert a scale at the axis level.
* project all the constraints at the finer scale.
* apply different Knowledge Sources (i.e. KS) on the MTG to compute the values at some nodes.
* solve the constraints.
* visualise the geometry using a 3D Turtle.

## Introduction
Let's import all we need for the tutorial.


```python
import k3d
from openalea.plantgl.all import *
from oawidgets.plantgl import *
```

## Data Reconstruction

We need to load some datasets from MTG


```python
from openalea.mtg import *
from openalea.deploy.shared_data import shared_data
data = shared_data(openalea.mtg)
```

    NOT using graph editor observer No module named grapheditor
    

First, we load the digitized Walnut [noylum2.mtg](https://mtg.readthedocs.io/en/latest/_downloads/ed0f93e9e03a91e86d350d86658198b2/noylum2.mtg)


```python
g = MTG(data/'noylum2.mtg')
```

Then, a file containing a set of default geometric parameters is loaded to build a DressingData ([walnut.drf](https://mtg.readthedocs.io/en/latest/_downloads/5ca37c29dc1a7f83e491f15457b0e547/walnut.drf))


```python
drf = data/'walnut.drf'
dressing_data = dresser.dressing_data_from_file(drf)
dressing_data = plantframe.DressingData(DiameterUnit=10)
```

    
    

## Visualisation of a digitized Tree

Geometric parameters are missing. How to compute them? Use the PlantFrame, a geometric solver working on multiscale tree structure.

Create the solver and solve the problem


```python
pf = plantframe.PlantFrame(g,
                       TopDiameter='TopDia',
                       DressingData = dressing_data)
```

Visualise the plant in 3D


```python
scene = pf.plot(gc=True, display=False)
PlantGL(scene)
```


    UGxvdChhbnRpYWxpYXM9MywgYXhlcz1bJ3gnLCAneScsICd6J10sIGJhY2tncm91bmRfY29sb3I9MTY3NzcyMTUsIGNhbWVyYT1bNC41LCA0LjUsIDQuNSwgMC4wLCAwLjAsIDAuMCwgMS4wLCDigKY=
    

