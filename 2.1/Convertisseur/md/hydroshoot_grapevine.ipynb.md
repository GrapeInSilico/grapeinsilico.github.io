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
from os import getcwd
from oawidgets.plantgl import *
from oawidgets.mtg import *
from openalea.mtg import traversal
from openalea.plantgl.all import Scene
from hydroshoot import architecture, display, model
```

    NOT using graph editor observer No module named grapheditor
    

We load the shoot architecture of a vine from plant digitalization data with HydroShoot which will return a Multi-scale Tree Graph. Then, we display it.


```python
# Path for plant digitalization data.
g = architecture.vine_mtg('grapevine_pot.csv')

plot(g)
```





<iframe
    width="900px"
    height="800px"
    src="html/graph_9134.html"
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


```python
scene = display.visu(g, def_elmnt_color_dict=True, scene=Scene(), view_result=False)
PlantGL(scene)
```


    UGxvdChhbnRpYWxpYXM9MywgYXhlcz1bJ3gnLCAneScsICd6J10sIGJhY2tncm91bmRfY29sb3I9MTY3NzcyMTUsIGNhbWVyYT1bNC41LCA0LjUsIDQuNSwgMC4wLCAwLjAsIDAuMCwgMS4wLCDigKY=
    


With the MTG() function, we can visualize a particuliar property of the MTG through a different colormap. 
For instance, we display the vine considering the length of every part of the shoot.


```python
MTG(g, 'Length')
```


    UGxvdChhbnRpYWxpYXM9MywgYXhlcz1bJ3gnLCAneScsICd6J10sIGJhY2tncm91bmRfY29sb3I9MTY3NzcyMTUsIGNhbWVyYT1bNC41LCA0LjUsIDQuNSwgMC4wLCAwLjAsIDAuMCwgMS4wLCDigKY=
    


## Simulation of hydraulic structure, gas and energy exchange dynamics

Once we tested some basic features, we run the model and simulate hydraulic structure, gas and energy exchange dynamics of the shoot.


```python
model.run(g, str(getcwd()) + '/', scene, psi_soil=-0.5, gdd_since_budbreak=1000., view_result=False)
```

    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    + Project:  /home/bbrument/oawidgets/example/hydroshoot_tutorial/
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    GDD since budbreak = 1000 °Cd
    Energy_budget: True
    Hydraulic structure: True
    Computing form factors...
    ... pirouette
    ... cacahuete
    Soil class: Sand
    rhyzo_solution: True
    Computing Nitrogen profile...
    ========================================================================
    Date 2012-08-01 11:00:00 
    
    psi_error =  0.02 :: Nb_iter = 7 ipsi_step = 0.500000
    t_error =  3.313 counter = 0 t_iter =  9 it_step =  0.5
    psi_error =  0.0 :: Nb_iter = 1 ipsi_step = 0.500000
    t_error =  1.025 counter = 1 t_iter =  7 it_step =  0.5
    psi_error =  0.0 :: Nb_iter = 1 ipsi_step = 0.500000
    t_error =  0.341 counter = 2 t_iter =  5 it_step =  0.5
    psi_error =  0.0 :: Nb_iter = 1 ipsi_step = 0.500000
    t_error =  0.121 counter = 3 t_iter =  3 it_step =  0.5
    psi_error =  0.0 :: Nb_iter = 1 ipsi_step = 0.500000
    t_error =  0.043 counter = 4 t_iter =  2 it_step =  0.5
    psi_error =  0.0 :: Nb_iter = 1 ipsi_step = 0.500000
    t_error =  0.015 counter = 5 t_iter =  0 it_step =  0.5
    ---------------------------
    psi_soil -0.5
    psi_collar -0.5015
    psi_leaf -0.5118
    
    gs 0.367819455871
    flux H2O 183.7813
    flux C2O 7.3977
    Tleaf  27.03 Tair  26.84
    
    ========================================================================
    
    ('beg time', datetime.datetime(2019, 7, 15, 10, 6, 12, 188165))
    ('end time', datetime.datetime(2019, 7, 15, 10, 7, 13, 500154))
    --- Total runtime: 1 minute(s) ---
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>An</th>
      <th>E</th>
      <th>Rg</th>
      <th>Tleaf</th>
    </tr>
    <tr>
      <th>time</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012-08-01 11:00:00</th>
      <td>7.397664</td>
      <td>183.781333</td>
      <td>84.879835</td>
      <td>27.031115</td>
    </tr>
  </tbody>
</table>
</div>



The same way we visualized the "Length" property, we can visualize now more specific property once the model is run.
For instance, we display the shoot through the **stomatal conductance** property.


```python
MTG(g, 'gs')
```


    UGxvdChhbnRpYWxpYXM9MywgYXhlcz1bJ3gnLCAneScsICd6J10sIGJhY2tncm91bmRfY29sb3I9MTY3NzcyMTUsIGNhbWVyYT1bNC41LCA0LjUsIDQuNSwgMC4wLCAwLjAsIDAuMCwgMS4wLCDigKY=
    

