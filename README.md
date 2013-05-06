Jervis Muindi   
Numerical Algorithms and Complexity    
Jenkins-Traub Algorithm
May 2013
Extra Credit

Introduction
============
This project contains code that provides an implementation of the Jenkin-Traub Algorithm. 

This algorithm is a faster than Newton method (which has order 2 AKA quadratic convergence) for finding the roots of polynomials. It can handle complex coefficients and roots and does not suffer from stability issues.

For an overview of the algorithm, the [Wikipedia article on the algorithm](https://en.wikipedia.org/wiki/Jenkins–Traub_algorithm) is a good starting point. More complete details can be found in the original Paper published by Jenkins and Traub in 1969.


How to Run
==========

You
<pre>
   python main.py -p [Polynomial] -e [error]
         Where:
         [Polynomial] Required Parameter. This is a listing of all coefficients of the polynomial. The listing goes from the highest degree term and proceed to lower degree terms. All coefficients of all terms must be explicitly listed. Lastly remember to use a space to separate the number.
         [error] Error bound to use on the roots. This is an optional parameter and it defaults to 10^(-6) if not specified
</pre>

For Example:    
To find the roots of the polynomial x^5 - 9.01*x^4 + (27.08)*x^3 -(41.19)*x^2 + (32.22)*x +  - 10.1
You can do the following
`python main.py -p 1, -9.01, 27.08, -41.19, 32.22, -10.1`


Sample Output
============
Below is some sample output obtained from running the program on the suggested polynomial above:
Polynomial = x^5 - 9.01*x^4 + (27.08)*x^3 -(41.19)*x^2 + (32.22)*x +  - 10.1

<pre>
Finding Roots for the Polynomial:
 (1.0+(0.0*I))*x^5 + (-9.01+(0.0*I))*x^4 + (27.08+(0.0*I))*x^3 + (-41.
19+(0.0*I))*x^2 + (32.22+(0.0*I))*x^1 + (-10.1+(0.0*I))*x^0

Using Error Value of: 1e-06

Starting Root Search ...
Success Stage Two terminated correctly at L = 1
Stage 3 was successful
Root is estimated to be at (0.999853310377+5.99742837711e-05j)
Success Stage Two terminated correctly at L = 1
Stage 3 was successful
Root is estimated to be at (1.01014824065-5.93584772307e-05j)
Success Stage Two terminated correctly at L = 3
Stage 3 was successful
Root is estimated to be at (0.999999646176+1.0000002704j)
Success Stage Two terminated correctly at L = 1
Stage 3 was successful
Root is estimated to be at (0.999998897167-1.00000085204j)
Success Stage Two terminated correctly at L = 1
Stage 3 was successful
Root is estimated to be at (4.99999990563-3.41668142667e-08j)
Root Search Complete

*********************

For The Polynomial
(1.0+(0.0*I))*x^5 + (-9.01+(0.0*I))*x^4 + (27.08+(0.0*I))*x^3 + (-41.1
9+(0.0*I))*x^2 + (32.22+(0.0*I))*x^1 + (-10.1+(0.0*I))*x^0
The roots found in order of increasing magnitude are:
1) (0.999853310377+5.99742837711e-05j)
2) (1.01014824065-5.93584772307e-05j)
3) (0.999999646176+1.0000002704j)
4) (0.999998897167-1.00000085204j)
5) (4.99999990563-3.41668142667e-08j)
</pre>
