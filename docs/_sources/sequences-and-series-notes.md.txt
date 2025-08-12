---
title: "Notes on Sequences and Series"
date: "2022-10-06"
categories:
  - "math"
---

# Sequences and Series: Some Preliminary Notes

I've been on a self-imposed deadline to get through a certain number of Professor Leonard's lectures on Sequences and Series.[^1]
As fun as "death-watching" his these excellent lectures can be, it quickly dawned on me that I needed to consolidate what I was learning, hence these notes.

## The Lay of the Land, Sequences vs. Series

## Sequences

A sequence is an ordered list of numbers.  We often denote sequences as $a_n$ or $\lbrace{a_n}\rbrace$, and we can specify the terms with a subscript, $a_1$ for the first term, $a_2$ for the second, etc. We can specify the terms either with a list, e.g. $a_n = \lbrace1, 4, 9, ... n\rbrace$ or with a formula $a_n = n^2$ 

Note that $n$ is always a positive integer.  In Calculus 2, n typically runs from 1 to infinity, but it's possible to specify other places to stop and start. Thus, if we were leading a band, we could start the song by counting from one to four, $\lbrace a_n \rbrace{^{4}_{n=1}} = n$.  

## Series

A series is very similar to a sequence, except it represents a sum of a squence of terms.  We typically represent a series using summation notation, so an example of a finite series adding the first three square numbers would be:

$$\sum_{n=1}^{3} n^2 = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14$$

The term $n=1$ at the bottom is our starting point, the 3 on the top is our endpoint, and the function $n^2$ tells us how to generate each term. Often we find it convenient to begin at one or zero, and much of our concern for Calculus 2 is to find whether the converges or diverges at infinity. That is to say, if we look at several partial sums of the series ${S_n}$ do these sums approach a number (converge) or not (diverge)? The limit at infinity is the 

## Properties of Infinite Series (p. 612)

$
\begin{aligned} \sum_{n=1}^\infty c \cdot a_n = c \cdot \sum_{n=1}^\infty a \end{aligned} \\ 
$ 


$
\begin {aligned}
\sum_{n=1}^\infty (a_n \pm  b_n)  = \sum_{n=1}^\infty a_n \pm \sum_{n=1}^\infty b_n 
\end{aligned}
$

## Tests for Convergence and Divergence

### nth Term Test for Divergence nth-Term Test for Divergence
Prof. Leonard suggests we apply this test early on if we can if the limit of the series is easy to find.  The important theorem to remember here is the converse of this theorem:

$$\text{If}\sum_{n=1}^\infty a_n \text{converges, then} \lim_{n \to \infty} a_n = 0$$

Though we can't use this to test for convergence, we can use its opposite to demonstrate convergence:

#### Divergence test theorem:
$$\text{If} \lim_{n \to \infty} a_n \ne 0 \text{ then} \sum_{n=1}^\infty a_n \text{ diverges.}$$

### Geometric Series (p 610)

A geometric series takes the general form of a constant multiplied by a base raised to the successive powers of $n$, beginning from zero. That is to say, it takes the general form of:

$$\sum_{n=0}^\infty ar^n = a + ar + ar^2 + ... ar^n + ..., \text{ where } a \ne 0$$

A geometric series with a base $r$ diverges if $|r| \ge 1$.  If $0 < |r| < 1$, then the series converges based on the following formula for geometric series:

$$\sum_{n = 0}^\infty ar^n = \frac{a}{1 -r}, 0 < |r| < 1$$

Although we don't often care about the sum at infinity, in this case we have a general formula for it.

### p-Series and Harmonic Series

In a geometric series, we have a constant times a fixed base raised successive powers, $n$.  In a p-Series, in contrast, we have a fixed numerator of 1, and in the denominator, we raise each successive term to a constant (postive) power ("p"), thus:

$$ \sum_{n=1}^\infty \frac{1}{n^p} = \frac{1}{1^p} + \frac{1}{2^p} + \frac{1}{3^p}$$

#### Harmonic Series as a special case:

A harmonic series is simply the case where $p = 1$, so we get a series of diminishing fractions:

$$ \sum_{n=1}^\infty \frac{1}{n} = \frac{1}{1} + \frac{1}{2} + \frac{1}{3}$$

#### p-Series Convergence and Divergence

A p-series converges if $p > 1$, and diverges if $0 < p \le 1$.  This tells us that a harmonic series, where $p = 1$ is divergent. 

### The Integral Test

Theorem:  If $f$ is positive, continuous, and decreasing for $x \ge 1$ and $a_n = f(n)$, then 

$$\sum_{n=1}^\infty a_n \text{ and}\int_1^\infty f(x)\space dx$$ 

either both converge or both diverge.

### Comparison Tests

#### Direct Comparison Test

Take two series.  Let $0 \lt a_n \le b_n$.

$$\text{If } \sum_{n=1}^\infty b_n \text{ converges, then } \sum_{n=1}^\infty a_n \text{ converges.}$$ 
$$\text{If } \sum_{n=1}^\infty a_n \text{ diverges, then } \sum_{n=1}^\infty b_n \text{ diverges.}$$ 

Given a series and another one based on it (that is simpler, typically, that's the point), if the "larger" series converges, the smaller one must also converge. If the smaller series diverges, the larger one must also diverge.  

[^1]: These notes are based on videos 9.1 through 9.9 in the [Calc 2 Playlist](https://www.youtube.com/results?search_query=calc+2+professor+leonard+playlist), and Chapter 9 of **Calculus: Early Transcendental Functions**, Ron Larson and Bruce Edwards, 5th Edition.

#### Limit Comparison Test
For a geometric series or P-series, it might be difficult to do direct comparison test.  In that case, we can use Limit Comparison Test:

Theorem:

Suppose that $a_n > 0, b_n > 0$, and 

$$\lim_{n \to \infty} (\frac{a_n}{b_n} )= L$$

where $L$ is finite and positive.  Then the two series, $\sum a_n$ and $\sum b_n$, either both converge or both diverge.  Note that for this to work, $a_n$ is the original series (in the numerator).  The comparison series is in the denominator.

### Alternating Series Test

In an alternating series, the signs alternate, so formally, the series looks like:

$$\sum_{n=1}^\infty (-1)^n \space a_n\text{ or } \sum_{n=1}^\infty (-1)^{n-1} \space a_n$$


The two forms depend on whether we want to start off negagtive or positive (We can also adjust the starting point to zero and adjust terms accordingly).  To be alternating, the series must alternate "every other sign", not two positive followed by two negative, for example.

Theorem: 

Such an alternating series converges if the following two conditions are met:

$$ \text{1. } \lim_{n \to \infty} a_n = 0 $$
$$ \text {2. } a_{n-1} \le a_n \text{ for all } n $$
 
To prove the second point, that the function is descending everywhere, we take this approach:  let $a_n = f(x)$, then we can show that $\frac{d}{dx} f(x)$ is negative for the domain we're considering.  Remember ascending and descending functions from Calc 1. 

### Alternating Series Remainder

Todo:  review as needed c.f. L&E page 635.

### Absolute Convergence

Some series with different signs do not strictly alternate, such as:

$$ \sum_{n=1}^\infty \frac{\sin n}{n^2} $$

We can see if the series of the terms absolute values converge -- if so, it is "absolutely convergent."  In this case, since $ | \sin n| \le 1 $ for all n, for all $ n > 1$, 

$$ \left| \frac{\sin n}{n^2} \right| <= \frac{1}{n^2} $$

Therefore the series converges.  This means that the series without the absolute value converges.

Absolute convergence is the stronger claim.  

Theorems and definitions:

If the series $\sum \space |a_n|$ converges, then the series $\sum a_n$ converges.  This is absolute convergence.

If the series $\sum \space |a_n|$ does not converge but the series $\sum a_n$ does, the series is conditionally convergent.

### The Ratio Test and Root Test

#### The Ratio Test

Let $\sum a_n$ be a series with non-zero terms.

Then:

$
\begin{aligned}
\lim \limits_{n \to \infty} \left| \frac{a_n + 1}{a_n} \right| < 1 \text{ converges absolutely.}\\
\end{aligned}
$

$
\begin{aligned}
\lim \limits_{n \to \infty} \left| \frac{a_n + 1}{a_n} \right| > 1 \space (\text{or } \infty ) \text{ diverges.}\\
\end{aligned}
$

$
\begin{aligned}
\lim \limits_{n \to \infty} \left| \frac{a_n + 1}{a_n} \right| = 1 \text{ is inconclusive.}\\ 
\end{aligned}$

#### The Root Test

Not as useful as the ratio test, TODO.


