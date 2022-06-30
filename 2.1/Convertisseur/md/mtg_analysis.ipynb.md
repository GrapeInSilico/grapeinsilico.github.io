# MTG Tutorial - Analysis

[MTG](https://mtg.readthedocs.io/) is an [OpenAlea](https://openalea.readthedocs.io/) model. MTG (Multiscale Tree Graph) allows to represent plant architecture on a graph at different scales.

Basically, a MTG is topological data that could be extracted with requests, as a data base.

In this **tutorial**, we will work on a part of a Noylum MTG.

For that we will follow different steps:

* Load the tree digitised MTG
* Explore the MTG as an architectural database
  * number of vertices
  * class of vertices
  * number of scales
  * properties
  
In order to make all these graphs, we used [pyvis](https://pyvis.readthedocs.io/).

## Introduction

First, let's import the **packages** we need for the tutorial.


```python
import openalea
from openalea.mtg import *
from openalea.deploy.shared_data import shared_data
from oawidgets.mtg import plot
from oawidgets.plantgl import PlantGL
```

    NOT using graph editor observer No module named grapheditor
    

Some **conventions** :
* MTG data structure : **g**
* Vertex identifier: **vid**

## Load and Display the MTG 

Now, we collect MTG data.


```python
data = shared_data(openalea.mtg)
g = MTG(data/'boutdenoylum2.mtg')
```

We plot the MTG. **Different colors represent different complexes** and each complex begins with a box node which is the **component root**.

Notice that you can **click and drag** on a particuliar node to make it move. Also, you can see some properties of the node by **putting you mouse over** a node.


```python
plot(g)
```





<iframe
    width="900px"
    height="800px"
    src="html/graph_2856.html"
    frameborder="0"
    allowfullscreen
></iframe>




## MTG Extraction and Visualisation

### Scales and Classes represent modularities

#### Scale 1 : P = Plant

#### Scale 2 : A = Axes

#### Scale 3 : Growth Unit
* S : Shoot
* U : Unit


Let's find the **number of scales** 'nb_scales()' in the MTG and print how many vertices per scale and the classes in each scale.


```python
nb_scales = g.nb_scales()

# Print the vertices at different scales
for scale in range(1, nb_scales):
    print 'Nb vertices at scale ', scale, ': ', g.nb_vertices(scale=scale)
    print 'Classes : ', ', '.join(list(set(g.class_name(vid) for vid in g.vertices(scale=scale))))
```

    Nb vertices at scale  1 :  1
    Classes :  P
    Nb vertices at scale  2 :  63
    Classes :  A
    Nb vertices at scale  3 :  198
    Classes :  S, U
    

Actually, the **default scale** is the max scale (3 here) but you can change it to plot it at a different scale.

You will notice that all the nodes have the same color. Being at lower scale, there is only one group defined, so there is only one color.


```python
plot(g, scale=g.max_scale()-1)
```





<iframe
    width="900px"
    height="800px"
    src="html/graph_1412.html"
    frameborder="0"
    allowfullscreen
></iframe>




We can select **all the vertices of each class**.


```python
classes = list(set(g.class_name(vid) for vid in g.vertices() if g.class_name(vid)))
print classes

def vertices(g, class_name='P'):
    return [vid for vid in g.vertices() if g.class_name(vid)==class_name]

vids_U = vertices(g, 'U')
print 'Nb U', len(vids_U)
```

    ['A', 'P', 'S', 'U']
    Nb U 84
    

Let's plot the graph with the selected vertices corresponding to the **U class**.


```python
plot(g, selection=vids_U)
```





<iframe
    width="900px"
    height="800px"
    src="html/graph_8522.html"
    frameborder="0"
    allowfullscreen
></iframe>




### Property Extraction

Let's go on by **displaying a whole property** through the graph.


```python
# Properties on the MTG: this exclude all the topological properties
print g.property_names()

# Retrieve one property for the MTG (dict)
phi = g.property('phi')
```

    ['Nf', 'YY', 'edge_type', 'Az1', '_line', 'index', 'label', 'TopDia', 'phi', 'psi', 'Azm', 'XX', 'ZZ', 'El1', 'NFe', 'Dist', 'Lum4', 'Lum2', 'Lum3', 'Lum1', 'teta', 'position', 'Inc']
    

Once you've extracted the **'phi' property** corresponding to the $\phi$ angle. You can **change the labels** of the graph nodes with it.

Now, if you **zoom** in a node, you will see that the labels have changed.


```python
plot(g, labels=phi)
```





<iframe
    width="900px"
    height="800px"
    src="html/graph_9931.html"
    frameborder="0"
    allowfullscreen
></iframe>




### Trunk Extraction

In this part, we will select and visualise the **trunk**.


```python
root = g.roots_iter(scale=g.max_scale()).next()
trunk = g.Trunk(root)
```

Now we have the **selection of the trunk**, we can visualise it.


```python
plot(g, selection=trunk)
```





<iframe
    width="900px"
    height="800px"
    src="html/graph_9325.html"
    frameborder="0"
    allowfullscreen
></iframe>




### Leaves Extraction

Let's select the **leaves** and display them.


```python
leaves = [vid for vid in g.vertices(scale=g.max_scale()) if g.is_leaf(vid)]
plot(g, selection=leaves)
```





<iframe
    width="900px"
    height="800px"
    src="html/graph_6461.html"
    frameborder="0"
    allowfullscreen
></iframe>




### Component Roots Extraction

Now, we select the **first component of each complex**, which are **the component roots**. In fact, the MTG is built at different scale, so we want to highlight the nodes that represent a complex at one lower scale.


```python
c_roots = [g.component_roots_at_scale_iter(cid, scale=g.max_scale()).next() for cid in g.vertices(scale=g.max_scale()-1)]
plot(g, selection=c_roots)
```





<iframe
    width="900px"
    height="800px"
    src="html/graph_3760.html"
    frameborder="0"
    allowfullscreen
></iframe>




### Descendants Extraction

Here, we select all the **descendants** of one particuliar node.


```python
root_id = 139
children = g.Descendants(root_id)
plot(g, selection=children)
```





<iframe
    width="900px"
    height="800px"
    src="html/graph_4187.html"
    frameborder="0"
    allowfullscreen
></iframe>




## PlantFrame 3D 

Now, we can **display the MTG in 3D**. You can check the [PlantFrame tutorial](https://nbviewer.jupyter.org/github/openalea/openalea.rtfd.io/blob/master/example/mtg_plantframe.ipynb).


```python
drf = data/'walnut.drf'
dressing_data = dresser.dressing_data_from_file(drf)
dressing_data = plantframe.DressingData(DiameterUnit=10)
pf = plantframe.PlantFrame(g, TopDiameter='TopDia', DressingData = dressing_data)
scene = pf.plot(gc=True, display=False)
PlantGL(scene)
```

    
    


    UGxvdChhbnRpYWxpYXM9MywgYXhlcz1bJ3gnLCAneScsICd6J10sIGJhY2tncm91bmRfY29sb3I9MTY3NzcyMTUsIGNhbWVyYT1bNC41LCA0LjUsIDQuNSwgMC4wLCAwLjAsIDAuMCwgMS4wLCDigKY=
    

