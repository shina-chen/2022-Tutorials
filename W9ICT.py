"""
W9 ICT 

21st Sep 2022

Shina  (In-person) 

"""


import numpy as np 
import matplotlib.pyplot as plt 
# one_array  = np.arange(0, 5, dtype = int) 
# print (one_array) 


"""
type (1) 
Out[2]: int

type (1.)
Out[3]: float

with a dot means its a float (with decimal) 

"""
# term = 1.0 
# one_array += term 
# print (one_array) 

"""
This creates an error shown below: 
UFuncTypeError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int32') with casting rule 'same_kind'
"""

# int = ... -1, 0, 1, 2,3, 
# float = 0.1, 0.

#Think about how are these values are actually stored in a computer 

#int32 
#Integer number stored with 32 bits 


#This works when change dtype to float 
"""
one_array  = np.arange(0, 5, dtype = float) 
term = 1.0
one_array += term 
print (one_array) 
#This works 

"""


# data = [1,2,3,4,5 ]

# one_array = np.ones_like(data, dtype = float)
# # copy the shape and the dtype 

# term = 1.0 
# one_array += term 

# print (one_array) 

#######################################################
#           Question            # 
#######################################################

#Initial conditions 
u0 = 1 #arbitary  
L = 10
fig,ax = plt.subplots() 


#Looks like for loop but don't use it! too tedious 
# f = [] 
# for x 



x = np.linspace (0, L, num = 51) 
f = np.where (
    x < L/2,        # Conditional 
    2*u0/L * x,     # if conditional == True: 
    2*u0/L * (L-x)  # else: 
)

ax.plot(x,f) 
plt.show() 


#If we want time, need a 3D plot instead of 2D (in space) 


fix,ax = plt.subplots (subplot_kw = {"projection": "3d"})

#2 ways of 3D (wireframe or surface) 
# ax.plot_surface(...) 
# ax.plot_wirframe(...) 

x, t= np.meshgrid ( #the grid will be 2D, need to provide 2 sets of data
    np.linspace (0, L, num = 51),    #space dimension 
    np.linspace (0 ,5, num = 21),    #time dimension
    indexing = 'ij' 
 )


# print (x) #to check 
# print (t) #check 


f = np.where (
    x < L/2,        # Conditional 
    2*u0/L * x,     # if conditional == True: 
    2*u0/L * (L-x)  # else: 
)


# Fourier's method 
D = 1 

u = u0/2 - 16*u0/(np.pi)**2 * \
    ((0.25* np.exp(-D* (2*np.pi/L)**2 * t)) * \
        np.cos(2*np.pi*x/L) + 1/36 * \
            (np.exp(-D*(6*np.pi/L)**2*t))*np.cos(6*np.pi*x/L))

print (u) 
    
ax.plot_surface(x,t, u)     






















