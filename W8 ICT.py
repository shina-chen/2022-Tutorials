"""

W8 ICT

14th Sep 2022

Shina

"""


import numpy as np 
import matplotlib.pyplot as plt 
from numpy.fft import fft, ifft, fftfreq, fftshift

f = np.array ([1, 2-1j, -1j, -1+2j])
print (f"Data points: {f}")

# Do by hand to practice/check 

#FFT coefficients 
a = fft(f) 
print (f"Coefficients : {a}")

check = ifft(a) 
error = np.abs(check-f)
print (f"Maximum reconstruction error: {np.max(error)}")




#Part 2a) 
#Not hard coding values of f 
N = 8 
n = np.arange(0,N) 
f = np.sin(2*np.pi*n/N)  #don't reuse variables a & f, bad coding 

_, ax = plt.subplots() 
ax.plot (n,f) 
plt.show() 

a = fft(f) #coefficients from fast fourier transform 

#Plot coefficients 

_,ax = plt.subplots () 
# ax.plot (n,a) # <-- complex! can't plot 
# ax. plot (n, a.real, label = "real") 
# ax.plot (n, a.imag, label = "Imaginary") 

#use fft shift & ffft frequency to generate better plots 
w = fftfreq(f.size, d=1) #Sample spacing (inv)
#assume d = 1 (frequency of how often sampled)

ax. plot (fftshift(w), a.real, label = "real") 
ax.plot (fftshift(w), a.imag, label = "Imaginary") 


ax.legend() 
plt.show() 

