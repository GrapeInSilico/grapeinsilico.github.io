# HydroShoot Tutorial - Grapevine

### Authors : R.Albasha, C.Fournier, C.Pradal, M.Chelle, J.A Prieto, G.Louarn, T.Simonneau, E.Lebon
### Publication : https://doi.org/10.1093/insilicoplants/diz007

[HydroShoot](https://hydroshoot.readthedocs.io) is a functional-structural plant model that simulates the interactions between shoot’s hydraulic structure, gas-exchange and energy-budget, at the organ level.

In this **tutorial**, we will :
* reconstruct in 3D the shoot architecture of a vine from plant digitalization data
* simulate hydraulic structure, gas and energy exchange dynamics

## 3D reconstruction of vine architecture

Let's import all the packages we need for this tutorial.


```python
from ipywidgets import IntSlider
from ipywidgets.embed import embed_minimal_html
import ipywidgets as widgets
from os import getcwd
from oawidgets.plantgl import *
from oawidgets.mtg import *
from openalea.mtg import traversal
from openalea.plantgl.all import Scene
from hydroshoot import architecture, display, model
```

We load the shoot architecture of a vine from plant digitalization data with HydroShoot which will return a Multi-scale Tree Graph. Then, we display it.


```python
# Path for plant digitalization data.
g = architecture.vine_mtg('grapevine_pot.csv')

```





<iframe
    width="900px"
    height="800px"
    src="mtg.html"
    frameborder="0"
    allowfullscreen

></iframe>





```python
# Local Coordinates Correction
for v in traversal.iter_mtg2(g, g.root):
    n = g.node(g.Trunk(v, Scale=1)[0])
    theta = 180 if int(n.index()) < 200 else -90 if int(n.index()) < 300 else 0
    architecture.vine_orientation(g, v, theta, local_rotation=True)

# Scene rotation
for v in traversal.iter_mtg2(g, g.root):
    architecture.vine_orientation(g, v, 90., local_rotation=False)

for v in traversal.iter_mtg2(g, g.root):
    architecture.vine_phyto_modular(g, v)
    architecture.vine_mtg_properties(g, v)
    architecture.vine_mtg_geometry(g, v)
    architecture.vine_transform(g, v)
```

Now, we create a scene from the MTG and we display it with the PantGL() function.

With the MTG() function, we can visualize a particuliar property of the MTG through a different colormap. 
For instance, we display the vine considering the length of every part of the shoot.


```python
slider = MTG(g, 'Length')
embed_minimal_html('export.html', views=[slider], title='Widgets export')
```


    Plot(antialias=3, axes=['x', 'y', 'z'], axes_helper=1.0, axes_helper_colors=[16711680, 65280, 255], background…


## Simulation of hydraulic structure, gas and energy exchange dynamics

Once we tested some basic features, we run the model and simulate hydraulic structure, gas and energy exchange dynamics of the shoot.

The same way we visualized the "Length" property, we can visualize now more specific property once the model is run.
For instance, we display the shoot through the **stomatal conductance** property.


```python
MTG(g, 'gs')
```


    Plot(antialias=3, axes=['x', 'y', 'z'], axes_helper=1.0, axes_helper_colors=[16711680, 65280, 255], background…

