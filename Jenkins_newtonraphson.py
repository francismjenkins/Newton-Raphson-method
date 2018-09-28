

# Python code for implementation of Newton Raphson method
# Author: Frank Jenkins

import matplotlib.pyplot as plt 

k = 0.0001 # the given tolerance level


def func(x): 
    return 0.5*x**3 - 4*x**2 + 5.5*x - 1
  
# Derivative of the above function  
def derivFunc(x): 
    return 1.5*x**2 - 8*x + 5.5 
# Function to find the root 
def newtonRaphson(x): 
    h = func(x) / derivFunc(x) 
    while abs(h) >= k: 
        h = func(x)/derivFunc(x) 
          
        x = x - h 
      
    return x
  
x1 = 0.5 # Initial values assumed 
print("The approximate value of the root is: ", newtonRaphson(x1))

x2 = 1.0
print("The approximate value of the root is: ", newtonRaphson(x2))

x3 = 6.0
print("The approximate value of the root is: ", newtonRaphson(x3))

if(func(newtonRaphson(x1)) <= k and func(newtonRaphson(x2)) <= k and func(newtonRaphson(x3)) <= k):
    print("All roots are within the given tolerance")
else:
    print("The roots are incorrect")

