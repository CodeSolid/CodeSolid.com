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
import sympy as sp
import matplotlib as mp
sp.init_session()
```

```{code-cell} ipython3
#%pip install plotly
```

```{code-cell} ipython3
a,b = symbols("a b")
```

```{code-cell} ipython3
a = 1
b = 3
```

```{code-cell} ipython3
ellipse =   (y**2)/(b**2) + (x**2)/(a**2) - 1 
hyperbola = (y**2)/(b**2) - (x**2)/(a**2) - 1 

# Another way to write function without zeroing out one side.
hyperbola2 = Eq((y**2)/(b**2) - (x**2)/(a**2), 1)
```

```{code-cell} ipython3
%matplotlib inline
p1 = plot_implicit(ellipse, show=False, xlabel="", ylabel="")
p2 = plot_implicit(hyperbola,show=False, xlabel="", ylabel="")
p1.extend(p2)
p1.show()
```

```{code-cell} ipython3
# Now do it Euclid's way.a
# Not sure why plot starts to break down at  radii > 5
%matplotlib inline
circle1 = Circle(Point(0,0), 5)
# print(circle1.center)
# print(circle1.radius)
# print(circle1.equation())
p = plot_implicit(circle1.equation(), show=False)
p.aspect_ratio=(1,1) 
grid_max = 10
grid_min = -10
lims = (grid_min, grid_max)
p.xlim = lims
p.ylim = lims
p.show()
```

```{code-cell} ipython3
from sympy import __version__
__version__
```

```{code-cell} ipython3

```
