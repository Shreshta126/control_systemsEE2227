import control
import matplotlib.pyplot as plt
import sys

#if using termux
import subprocess
import shlex
#end if


s = control.TransferFunction.s
GH=41*(s+4)/(s**2*(s+3))   #open looop transfer function G(s)H(s)
t=41/(s**3+3*s**2+41*s+164)

plt.figure(1)  # nyquist plot
control.nyquist(GH)   
plt.text(-1,0, "(-1,0)")
plt.title('Nyquist Plot of G(s)H(s)')
plt.grid(True)
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')

#if using termux
#plt.savefig('./figs/ee18btech11041_1.pdf')
#plt.savefig('./figs/ee18btech11041_1.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11041_1.pdf"))
#else


plt.figure(2) #zoomed in plot
control.nyquist(GH)   
plt.xlim(-2,1)
plt.ylim(-0.5,0.5)
plt.text(-1,0, "(-1,0)")
plt.title('Zoomed in Nyquist Plot of G(s)H(s)')
plt.grid(True)
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')

#if using termux
#plt.savefig('./figs/ee18btech11041_2.pdf')
#plt.savefig('./figs/ee18btech11041_2.eps')
#subprocess.run(shlex.split("termux-open ./figs/ee18btech11041_2.pdf"))
#else
#plt.show()
