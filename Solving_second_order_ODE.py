import numpy as np
from scipy.integrate import odeint
import math 
import matplotlib.pyplot as plt 


def model(theta,t,b,g,l,m):
    theta1 = theta[0]
    theta2 = theta[1]
    dtheta1_dt = theta2 
    dtheta2_dt = (b/m)*theta2 - (g/l)*math.sin(theta1)
    dtheta_dt = (dtheta1_dt,dtheta2_dt)
    return dtheta_dt

b = 0.02
g = 9.81 
l = 1 
m = 0.1 

#Initial condition
theta_0 = [0,5]
t = np.linspace(0,10,150)

theta = odeint(model,theta_0,t,args = (b,g,l,m))

plt.plot(t,theta[:,0],'b-')
plt.plot(t,theta[:,1],'r--')
plt.xlabel("time")
plt.ylabel("plot")
plt.legend(loc = 'best')
plt.show()
