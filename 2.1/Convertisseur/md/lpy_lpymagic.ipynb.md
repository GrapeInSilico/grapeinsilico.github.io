# LPy Tutorial - LPyMagic

L-systems were conceived as a mathematical framework for modeling growth of plants. [LPy](https://lpy.readthedocs.io) is a simulation software that mixes L-systems construction with the Python high-level modeling language.

In this **tutorial**, we will :
* use a magic allowing using LPy language in the notebook
* display some 3D plant architecture made with LPy

## Introduction

First, we need to import some packages for the tutorial.


```python
from oawidgets import lpymagic, plantgl
from random import *
```

    NOT using graph editor observer No module named grapheditor
    


```python
%reload_ext oawidgets.lpymagic
```

## LPy Magic and 3D-Visualisation

Now, we define the axiom and the construction rules.
The plant architecture is automatically displayed.


```python
p1 = 0.550000
p2 = 0.450000
axiom = "_(1)[f(50)+90f(10)]-(90)P(1,0)"
```


```python
%%lpy -i * -w axiom -n 100 -s scene


#Axiom: F(1)
derivation length: 100

# A = branching state
# B = non-branching state 

def Start():
    global m
    m = 0

production:

P(x,t) :
    if t <= 10 : produce T[G(x)]P(x,t+1)
    else  :
        global m
        m = 1
        produce *

G(x) : 
    if m==1 :
        produce +(90)S(x)

S(x) :
    if random() <= 0.5: produce A(x)
    else: produce B(x)

A(x) : 
    if random() <= p1: produce I[M(x)]A(1-x)
    else: produce IB(1-x)

B(x) :
    if random() <= p2: produce IB(1-x)
    else: produce I[M(x)]A(1-x)

homomorphism:

T :    produce ;(1)f(40);(1)@c(1)
M(x) : 
    if x==0 :   produce ;(2)+F(20)
    elif x==1 : produce ;(2)-F(20)

I    : produce ;(1)F(2)
A(x) : produce ;(1)@O(3)
B(x) : produce ;(2)@O(3)

endlsystem
```

    DEBUG:  _(1)[f(50)+90f(10)]-(90)P(1,0) 99 100
    


    UGxvdChhbnRpYWxpYXM9MywgYXhlcz1bJ3gnLCAneScsICd6J10sIGJhY2tncm91bmRfY29sb3I9MTY3NzcyMTUsIGNhbWVyYT1bNC41LCA0LjUsIDQuNSwgMC4wLCAwLjAsIDAuMCwgMS4wLCDigKY=
    

