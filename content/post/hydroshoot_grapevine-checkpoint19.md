+++
title ='HydroShoot Tutorial - Grapevine'
slug = 'post24'
description = '[HydroShoot](https://hydroshoot.readthedocs.io) is a functional-structural plant model that simulates the interactions between shoot’s hydraulic structure, gas-exchange and energy-budget, at the organ level.In this **tutorial**, we will :* reconstruct in 3D the shoot architecture of a vine from plant digitalization data'
disableComments = true
image = '/images/window/photo-1572360678077-0ab5ce1be418.jpg'
numero = 1
+++

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


    ---------------------------------------------------------------------------

    IOError                                   Traceback (most recent call last)

    <ipython-input-2-2de76fc3583b> in <module>()
          1 # Path for plant digitalization data.
    ----> 2 g = architecture.vine_mtg('grapevine_pot.csv')
          3 
          4 plot(g)
    

    /home/bbrument/miniconda3/envs/notebook_env/lib/python2.7/site-packages/hydroshoot-1.0.0-py2.7.egg/hydroshoot/architecture.pyc in vine_mtg(file_path)
        154 #connect_r -> connect_inI
        155 
    --> 156     table = read_csv(file_path,sep=';',decimal='.',header=0)
        157 
        158     g = mtg.MTG()
    

    /home/bbrument/miniconda3/envs/notebook_env/lib/python2.7/site-packages/pandas/io/parsers.pyc in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, doublequote, delim_whitespace, low_memory, memory_map, float_precision)
        676                     skip_blank_lines=skip_blank_lines)
        677 
    --> 678         return _read(filepath_or_buffer, kwds)
        679 
        680     parser_f.__name__ = name
    

    /home/bbrument/miniconda3/envs/notebook_env/lib/python2.7/site-packages/pandas/io/parsers.pyc in _read(filepath_or_buffer, kwds)
        438 
        439     # Create the parser.
    --> 440     parser = TextFileReader(filepath_or_buffer, **kwds)
        441 
        442     if chunksize or iterator:
    

    /home/bbrument/miniconda3/envs/notebook_env/lib/python2.7/site-packages/pandas/io/parsers.pyc in __init__(self, f, engine, **kwds)
        785             self.options['has_index_names'] = kwds['has_index_names']
        786 
    --> 787         self._make_engine(self.engine)
        788 
        789     def close(self):
    

    /home/bbrument/miniconda3/envs/notebook_env/lib/python2.7/site-packages/pandas/io/parsers.pyc in _make_engine(self, engine)
       1012     def _make_engine(self, engine='c'):
       1013         if engine == 'c':
    -> 1014             self._engine = CParserWrapper(self.f, **self.options)
       1015         else:
       1016             if engine == 'python':
    

    /home/bbrument/miniconda3/envs/notebook_env/lib/python2.7/site-packages/pandas/io/parsers.pyc in __init__(self, src, **kwds)
       1706         kwds['usecols'] = self.usecols
       1707 
    -> 1708         self._reader = parsers.TextReader(src, **kwds)
       1709 
       1710         passed_names = self.names is None
    

    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader.__cinit__()
    

    pandas/_libs/parsers.pyx in pandas._libs.parsers.TextReader._setup_parser_source()
    

    IOError: File grapevine_pot.csv does not exist



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

With the MTG() function, we can visualize a particuliar property of the MTG through a different colormap. 
For instance, we display the vine considering the length of every part of the shoot.


```python
MTG(g, 'Length')
```

## Simulation of hydraulic structure, gas and energy exchange dynamics

Once we tested some basic features, we run the model and simulate hydraulic structure, gas and energy exchange dynamics of the shoot.


```python
model.run(g, str(getcwd()) + '/', scene, psi_soil=-0.5, gdd_since_budbreak=1000., view_result=False)
```

The same way we visualized the "Length" property, we can visualize now more specific property once the model is run.
For instance, we display the shoot through the **stomatal conductance** property.


```python
MTG(g, 'gs')
```
