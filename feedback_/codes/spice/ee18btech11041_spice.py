import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('plotdata.data')  

data2=np.loadtxt('plotdata2.data')  

data3=np.loadtxt('plotdata3.data')  


plt.figure(1)
plt.title ('H from spice simulation')
plt.plot(data[:,0],data[:,1])
plt.ylabel('H')
plt.xlabel('frequency Hz')
plt.grid()


plt.figure(2)
plt.title ('G from spice simulation')
plt.plot(data2[:,0],data2[:,1])
plt.ylabel('G')
plt.xlabel('frequency Hz')
plt.grid()


plt.figure(3)
plt.title ('T from spice simulation')
plt.plot(data3[:,0],data3[:,1])
plt.ylabel('T')
plt.xlabel('frequency Hz')
plt.grid()

plt.show()

