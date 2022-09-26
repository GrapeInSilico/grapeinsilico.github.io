+++
title ='Caribu Tutorial'
slug = 'hundred_page'
description = 'CaribuScene 2'
disableComments = true
image = '/images/window/images.jpg'
+++

# Caribu Tutorial Agagin


[test](/test.html)

<html> 
  <body>
  <iframe width=1000 height=900 src="/test.html" seamless></iframe>


  </body>
</html>



sdqdjknsqld


```python
import openalea.plantgl.all as pgl
from alinea.caribu.CaribuScene import CaribuScene
from alinea.caribu.data_samples import data_path

can = str(data_path('f331s1_100plantes.can'))
sky = str(data_path('Turtle16soc.light'))
opts = map(str, [data_path('par.opt'), data_path('nir.opt')])
#pattern = str(data_path('filter.8'))
    
# complete set of files
cs = CaribuScene(scene=can, light=sky, opt=opts, ) #pattern=pattern)
raw,agg=cs.run(simplify=True)
```

    NOT using graph editor observer No module named grapheditor
    


```python
scene,values = cs.plot(raw['par']['Ei'],display=False)
```


```python
import numpy as np
v99 = np.percentile(values, 99)
nvalues=np.array(values)
nvalues[nvalues>v99]=v99
values = nvalues.tolist()
```


```python
from oawidgets.plantgl import *
PlantGL(scene, group_by_color=False, property=values)
```


    UGxvdChhbnRpYWxpYXM9MywgYXhlcz1bJ3gnLCAneScsICd6J10sIGJhY2tncm91bmRfY29sb3I9MTY3NzcyMTUsIGNhbWVyYT1bNC41LCA0LjUsIDQuNSwgMC4wLCAwLjAsIDAuMCwgMS4wLCDigKY=
    

