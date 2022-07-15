```python


import ipywidgets as widgets

widgets.IntSlider()
```


    IntSlider(value=0)



```python
from IPython.display import display
w = widgets.IntSlider()
display(w)
```


    IntSlider(value=0)



```python


display(w)

w.close()
```


    IntSlider(value=0)



```python


w = widgets.IntSlider()
display(w)
w.value
w.value = 100
```


    IntSlider(value=0)



```python


widgets.Text(value='Hello World!', disabled=True)


```


    Text(value='Hello World!', disabled=True)



```python
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)

mylink = widgets.jslink((a, 'value'), (b, 'value'))
```


    FloatText(value=0.0)



    FloatSlider(value=0.0)

