from ipywidgets import IntSlider
from ipywidgets.embed import embed_minimal_html
import ipywidgets as widgets
from os import getcwd
from oawidgets.plantgl import *
from oawidgets.mtg import *
from openalea.mtg import traversal
from openalea.plantgl.all import Scene
from hydroshoot import architecture, display, model

g = architecture.vine_mtg('grapevine_pot.csv')

plot(g)

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

MTG(g, 'Length')

slider = IntSlider(value=40)
embed_minimal_html('export.html', views=[slider], title='Widgets export')