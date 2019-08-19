"""
 Program to calculate drag force
 By Sunil
"""
import matplotlib.pyplot as plt
#Inputs
c_d = 0.8 # Drag co-efficient for velocity vs drag force
c_d1 = [0.04,0.09,0.42,0.47,0.50,0.80] #Drag co-efficient in array for drag Coefficient vs drag force
A = 0.1 #Frontal area m^2
rho = 1.2 #Density kg/m^3
v = [5,6,7,8,9,10] #Velocity in array m/s
v1 = 5  #Velocity m/s


drag_force = []# drag forces array for velocity vs drag force
df = [] #drag force array  for drag Coefficient vs drag force



for velocity in v:
      drag_force.append(0.5*A*rho*c_d*velocity*velocity)

for c in c_d1:
    df.append(0.5 * A * rho * c * v1 * v1)
    print(df)

plt.plot(v,drag_force) #velocity vs drag force
plt.xlabel('velocity')
plt.ylabel('drag force')
plt.show() # To display velocity vs drag force
plt.plot(c_d1,df) #for drag Coefficient vs drag force
plt.ylabel('Coefficient of drag')
plt.xlabel('Drag Force')
plt.show() # To display coefficient of drag vs drag force