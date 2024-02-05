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
%pip install plotly
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

#focus1 = Point(-a, 0)
#focus2 = Point(a, 0)
```

```{code-cell} ipython3
#%matplotlib inline
p1 = plot_implicit(ellipse, show=False, xlabel="", ylabel="")
p2 = plot_implicit(hyperbola,show=False, xlabel="", ylabel="")
#p3 = plot_implicit(line,show=False, xlabel="", ylabel="")
#p4 = plot(1, show=False, xlabel="", ylabel="", line_color="red")

plot_implicit??
p1.extend(p2)
#p1.extend(p3)
#p1.extend(p4)
p1.show()
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
