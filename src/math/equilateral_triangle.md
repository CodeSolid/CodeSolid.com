---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
from sympy import init_session, sqrt, symbols
from sympy.geometry import Triangle, Circle, Point
from sympy.plotting.plot_implicit import plot_implicit
import matplotlib.pyplot as plt
```

```{code-cell} ipython3
%matplotlib inline

import numpy as np

def make_plottable(p1, p2):
    # converts ("flattens") two points to two arrays with x-value, y-value
    return [p1.x, p2.x],[p1.y, p2.y]

vertices = [Point(0,0), Point(10, 0), Point(5, 5* sqrt(3))]
t = Triangle(*vertices)

f, axes = plt.subplots(1)
axes.set_aspect(1)

for side in t.sides:    
    x, y = make_plottable(*side.points)
    axes.plot(x,y, color='black')


# theta goes from 0 to 2pi
theta = np.linspace(0, 2*np.pi, 200)

# the radius of the two circles == line AB
r = 10

# Left circle
# compute x1 and x2
x = r*np.cos(theta)
y = r*np.sin(theta)
axes.plot(x, y, color="gray", linewidth=".7")

# Right circle
x = r*np.cos(theta) + 10
y = r*np.sin(theta)
axes.plot(x, y, color="gray", linewidth=".7")

# Label vertices
axes.text(-1, 0, "A", fontsize='large')
axes.text(10.5, 0, "B", fontsize='large')
axes.text(4.5, 5 * sqrt(3) + .5, "C", fontsize='large')

# Label circles
axes.text(-11, 0, "D", fontsize='large')
_ = axes.text(20.3, 0, "E", fontsize='large')


          
```

See this page:  
https://www.cfm.brown.edu/people/dobrush/am33/SymPy/part1.html#plotting-geometric-entities

```{code-cell} ipython3
c1 = Circle(vertices[0], 10)
c2 = Circle(vertices[1], 10)
intersection = c1.intersect(c2)
vertices[2] in list(intersection)
```

# Circle graph by itself

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

# theta goes from 0 to 2pi
theta = np.linspace(0, 2*np.pi, 200)

# the radius of the circle
r = 10

# compute x1 and x2
x = r*np.cos(theta)
y = r*np.sin(theta)

# create the figure
fig, ax = plt.subplots(1)
ax.plot(x, y)
ax.set_aspect(1)
plt.show()
```

```{code-cell} ipython3

```
