import numpy as np
import matplotlib.pyplot as plt
h=int(input("enter the order of moving average system"))
Fs=2000
f1=50
f2=500
y=np.zeros(100)
t=np.linspace(0,4000,100)
a=np.sin(2*np.pi*f1*t/Fs)
b=np.sin(2*np.pi*f2*t/Fs)
x=a+b
sum=0
q=h-1
for i in range(0,100,1):
	for k in range(0,q,1):
		sum=sum+x[i-k]
	y[i]=float((sum)/(h))
	sum=0
print(y)
plt.subplot(411)
plt.plot(t,u)
plt.subplot(412)
plt.plot(t,v)
plt.subplot(413)
plt.plot(t,x)
plt.subplot(414)
plt.plot(t,y)
plt.show()
