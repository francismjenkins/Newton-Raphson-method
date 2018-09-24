
# coding: utf-8

# In[1]:



# Python code for implementation of Newton Raphson method

import matplotlib.pyplot as plt 


def func(x): 
    return 0.5*x**3 - 4*x**2 + 5.5*x - 1
  
# Derivative of the above function  
def derivFunc(x): 
    return 1.5*x**2 - 8*x + 5.5 
h = []
# Function to find the root 
def newtonRaphson(x): 
    h = func(x) / derivFunc(x) 
    while abs(h) >= 0.0001: 
        h = func(x)/derivFunc(x) 
          
        x = x - h 
      
    print("The approximate value of the root is : ", 
                             "%.4f"% x) 
  
x1 = 0.5 # Initial values assumed 
newtonRaphson(x1) 

x2 = 1.0
newtonRaphson(x2)

x3 = 6.0
newtonRaphson(x3)

