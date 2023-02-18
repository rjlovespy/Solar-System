import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


"""
Defining semimajor and semiminor distances of planets' orbits and Halley comet's orbit in AU
"""
p1_a, p1_e=0.3871, 0.206
p1_b= p1_a*np.sqrt(1-p1_e**2)
p2_a, p2_e=0.7223,0.007
p2_b= p2_a*np.sqrt(1-p2_e**2)
p3_a, p3_e=1,0.017
p3_b= p3_a*np.sqrt(1-p3_e**2)
p4_a, p4_e=1.5273,0.093
p4_b= p4_a*np.sqrt(1-p4_e**2)
p5_a, p5_e=5.2028,0.048
p5_b= p5_a*np.sqrt(1-p5_e**2)
p6_a, p6_e=9.5388,0.056
p6_b= p6_a*np.sqrt(1-p6_e**2)
p7_a, p7_e=19.1914,0.046
p7_b= p7_a*np.sqrt(1-p7_e**2)
#p8_a, p8_e=30.0611,0.010
#p8_b= p8_a*np.sqrt(1-p8_e**2)
HC_a, HC_e = 17.94, 0.967
HC_b= HC_a*np.sqrt(1-HC_e**2)


"""
Defining independent variables(t1,t2,t3,...,th) where
    1st parameter decides phase,
    2nd parameter decides period of revolution and,
    3rd parameter decides frames(stations) for overall animation of 18 objects
"""
t1=np.linspace(0,10*np.pi, 361)        # Mercury does 5 revoltions per Neptune's revolution around the Sun
t2=np.linspace(0,9*np.pi, 361)         # Venus does 4.5 revoltions per Neptune's revolution around the Sun
t3=np.linspace(0,8*np.pi, 361)         # Earth does 4 revoltions per Neptune's revolution around the Sun
t4=np.linspace(0,7*np.pi, 361)         # Mars does 3.5 revoltions per Neptune's revolution around the Sun
t5=np.linspace(0,6*np.pi, 361)         # Jupiter does 3 revoltions per Neptune's revolution around the Sun
t6=np.linspace(0,5*np.pi, 361)         # Saturn does 2.5 revoltions per Neptune's revolution around the Sun
t7=np.linspace(0,3*np.pi, 361)         # Uranus does 1.5 revoltions per Neptune's revolution around the Sun
t8=np.linspace(0,2*np.pi, 361)                
th=np.linspace(0,4*np.pi, 361)         # Halley Comet does 2 revoltions per Neptune's revolution around the Sun


"""
Defining dependent variables(x1(t1),y1(t1),x2(t2),y2(t2),....,xh(th),yh(th)) where 
centers of orbits lie at (a1e1,0),(a2e2,0),....,(aheh,0)
"""
x1=p1_a*np.cos(t1)-p1_a*p1_e
y1=p1_b*np.sin(t1)
x2=p2_a*np.cos(t2)-p2_a*p2_e
y2=p2_b*np.sin(t2)
x3=p3_a*np.cos(t3)-p3_a*p3_e
y3=p3_b*np.sin(t3)
x4=p4_a*np.cos(t4)-p4_a*p4_e
y4=p4_b*np.sin(t4)
x5=p5_a*np.cos(t5)-p5_a*p5_e
y5=p5_b*np.sin(t5)
x6=p6_a*np.cos(t6)-p6_a*p6_e
y6=p6_b*np.sin(t6)
x7=p7_a*np.cos(t7)-p7_a*p7_e
y7=p7_b*np.sin(t7)
# x8=p8_a*np.cos(t8) - p8_a*p8_e
# y8=p8_b*np.sin(t8)
xh=HC_a*np.cos(th)- HC_a*HC_e
yh=HC_b*np.sin(th)


"""
Initializing Objects for Animation
"""
fig=plt.figure()
ax=plt.axes(xlim=(-20.2,20.2), ylim=(-20.2,20.2))
mercury, =ax.plot(x1[0],y1[0],marker='o',markersize=3.25, markerfacecolor= 'fuchsia', label='Mercury')
mercury_o, =ax.plot(x1[0],y1[0],color='y',lw=1.5)
venus, =ax.plot(x2[0],y2[0],marker='o',markersize=3.5,markerfacecolor='gold', label='Venus')
venus_o, =ax.plot(x2[0],y2[0],color='y',lw=1.5)
earth, =ax.plot(x3[0],y3[0],marker='o',markersize= 4,markerfacecolor='dodgerblue',label='Earth')
earth_o, =ax.plot(x3[0],y3[0],color='y',lw=1.5)
mars, =ax.plot(x4[0],y4[0],marker='o',markersize=3.75,markerfacecolor='hotpink',label='Mars')
mars_o, =ax.plot(x4[0],y4[0],color='y')
jupiter, =ax.plot(x5[0],y5[0],marker='o',markersize= 6, markerfacecolor='lightpink',label='Jupiter')
jupiter_o, =ax.plot(x5[0],y5[0],color='y')
saturn, =ax.plot(x6[0],y6[0],marker='o',markersize=5.5,markerfacecolor='cyan', label='Saturn')
saturn_o, =ax.plot(x6[0],y6[0],color='y')
uranus, =ax.plot(x7[0],y7[0],marker='o',markersize=5,markerfacecolor='darkorange', label='Uranus')
uranus_o, =ax.plot(x7[0],y7[0],color='y')
#neptune, =ax.plot(x8[0],y8[0],marker='o',markersize=6.8, markerfacecolor='white', label='Neptune')
#neptune_o, =ax.plot(x8[0],y8[0],color='y')
halley, = ax.plot(xh[0],yh[0], marker='o',markersize= 5, markerfacecolor="lime",label='Halley')
halley_o, = ax.plot(xh[0],yh[0],color='y')


"""
Defining objects behaviour for animation 
"""
def solar_system(i):
  mercury.set_data(x1[i],y1[i])
  mercury_o.set_data(x1[i-10:i+1],y1[i-10:i+1])            # Generates a tail
  venus.set_data(x2[i],y2[i])
  venus_o.set_data(x2[i-10:i+1],y2[i-10:i+1])              # Generates a tail
  earth.set_data(x3[i],y3[i])
  earth_o.set_data(x3[i-10:i+1],y3[i-10:i+1])              # Generates a tail
  mars.set_data(x4[i],y4[i])
  mars_o.set_data(x4[i-10:i+1],y4[i-10:i+1])               # Generates a tail
  jupiter.set_data(x5[i],y5[i])
  jupiter_o.set_data(x5[i-10:i+1],y5[i-10:i+1])            # Generates a tail
  saturn.set_data(x6[i],y6[i])
  saturn_o.set_data(x6[i-10:i+1],y6[i-10:i+1])             # Generates a tail
  uranus.set_data(x7[i],y7[i])
  uranus_o.set_data(x7[i-10:i+1],y7[i-10:i+1])             # Generates a tail
  # neptune.set_data(x8[i],y8[i])
  # neptune_o.set_data(x8[i-10:i+1],y8[i-10:i+1])          # Generates a tail
  halley.set_data(xh[i],yh[i])
  halley_o.set_data(xh[i-15:i+1],yh[i-15:i+1])             # Generates a tail
  return mercury, mercury_o, venus, venus_o, earth, earth_o, mars, mars_o,jupiter, jupiter_o, saturn, saturn_o, uranus, uranus_o, halley, halley_o, #neptune, neptune_o, 
  
  
"""
Calling FuncAnimation function to animate the Solar System
"""
anime=animation.FuncAnimation(fig, solar_system, frames = len(th), interval=100, blit=True, repeat =True)
fig.suptitle("Solar System", color="fuchsia")
fig.patch.set_facecolor('k')
ax.plot(p1_a*p1_e,0,'ro',markersize=6.5, label='Sun')
ax.annotate("Courtesy of Rishikesh Jha",(16,-19), color="fuchsia")
ax.axis(False)
plt.legend()
# anime.save("Solar_System.gif")
plt.show()
