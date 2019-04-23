import matplotlib.pyplot as plt
import numpy as m
F=100
Fs=2000
n=m.arange(0,200,5)
A=m.sin((2*m.pi*F*n)/Fs)
plt.xlabel("time")
plt.ylabel("Amplitude")
plt.stem(n,A)
plt.show()
