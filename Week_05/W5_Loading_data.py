"""

W5 ICT 
Load data files

24/08/2022 

Author: Shina Chen

"""


import numpy as np 
import matplotlib.pyplot as plt 

#Pandas for more complex data-loader 

# data = np.loadtxt ("data_points.txt")
# print (data) #check 

# x = data[:, 0]
# f = data[:, 1]
# print (x)
# print (f) 

x,f  = np.loadtxt ("data_points.txt", unpack = True)

# print (x)
# print (f) 


#Part 2: Saving 

# data = np.column_stack ((x,f))

# np.savetxt ("output_file.txt", data, fmt = '%.4f') 


#Worksheet 

# P.T * P * x = P.T * f #(T = transpose)

# Quadratic equation - takes form of 
# ax^2 + bx^1 + c*x^0 
#   p2    p1      p0  (replaces the x^power)

# P = [p0, p1, p2] 

#turn into column vctor 
X = np.atleast_2d(x).T 
F = np.atleast_2d(f).T 


p0 = x**0 
p1 = x**1 
p2 = x**2 

P= np.column_stack((p0, p1, p2)) #Need as columns, not rows


a = np.linalg.inv(P.T @ P) @P.T @ F 


# fitted_trend = a[0] + a[1] * x + a[2]*x**2 

smooth_x = np.linspace (0,3) 
fitted_trend = a[0] + a[1] * smooth_x + a[2]*smooth_x**2 

# fig, ax = plt.subplots () 
fix, ax = plt.subplots () 


# ax.plot (x,f,'b-')
# ax.plot (x, fitted_trend, 'r') 

ax.scatter (x,f) 
ax.plot (smooth_x, fitted_trend, 'r') 

plt.show() 



#Question 2 

