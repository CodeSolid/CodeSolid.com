# Logarithms and Exponents

I feel like this area needed some review, so here are some notes on various things.  Logarithmic functions are inverse of exponential functions, so:

$$ y = log_a x \iff x = a^y $$

See these resources:

* [Logarithms -- How?](https://www.youtube.com/watch?v=Zw5t6BTQYRU)
* [Solving Logarithmic Equations...How?](https://www.youtube.com/watch?v=rBnQiLa2TYo)

## Easy examples

$ log_3\space9 $, think to yourself 3 to what power equals 9, but formally, do this, make it equal to x, i.e.
$ x = log_3\space 9 $.  Next use formula above so $ x = log_3\space 9 \iff 3^x = 9 $ therefore x = 2, or $ log_3\space 9 = 2 $.  With no base, e.g. $ log 10000 $, then base = 10, so equals $log_{10} \space10000 = x \iff x^10 = 10000 = 4$.

## Weirder logs

$ log_2\space\frac{1}{8} = x \iff 2^x = \frac{1}{8}.\space \therefore \space  x = -3$ 

Other weird ones:

$ log\space 1 (1); log\space0 (undefined); log\space(-1) (undefined)$

## Natural logs

$ ln\space1 = log_e\space1 $

Do same steps as before, set it to x and rearange to exponential form:

$ log_e\space1 = x \iff x^x = 1 \therefore x = 0 $

$ ln(e^3) $  Visually, this should be 3!  Do it long way:

$ ln_e (e^3) = x \iff e^x = e^3 \therefore x = 3 $

## Even weirder

$$ log_x\space32 = 5 \iff x^5 = 32 x = 2$$


$$ log_5x = 3 \iff 5^3 = x; x = 125$$

$$ Calculate log_2\space7 \iff 2^x = 7 $$ 

Change of base formula says we can do:

$$ \frac{log\space7}{log\space2} $$ 

You need to plug that into a calculator.  Answer by the way is 2.807354922057604.

## Log Properties

$ log_a(x * y ) =  log_a\space x + log_a\space y $

$ log_a\space(\frac{x}{y} ) =  log_a\space x -  log_a\space y $

$ log_a\space x^n  =  n\space log_a\space x $

## More solving

E.g. 

$$ \log\space (12x-7) = \log\space (3x+11) $$

Looks hard but if logs have same base, can just set insides = to each other and solve, so

$
	12x -7 = 3x + 11 \\ 
	9x = 18 \\
	x = 2
$

Based on equality property:

$$
log_b \space m = log_b \space m \iff m = n
$$

Note, need to plug answer back into original equation -- occasionally doesn't work.  Above we get $ log 17 = log 17 $.  If get negative number, have to throw it out because log of negative # is undefined.

Now, based on product property:


$ log_a(x * y ) =  log_a\space x + log_a\space y $

if have this problem:

$ \log_2 x + \log_2 (x-2) = 3 $

Equivalent to

$ \log_2 \space (x * (x -2)) \\
\log_2 \space \therefore \\
2^3 = x(x-2) \\
8 = x^2 - 2x \\
x^2 - 2x - 8 = 0 \\
(x -4)(x + 2) = 0 \\
x = 4, x = -2 \\
x = 4, \cancel{(x = 2)}
$

Have to plug back in... which leads us to throw out the -2 as it's a domain error.
$

