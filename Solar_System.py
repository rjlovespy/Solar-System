from matplotlib.animation import writers
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

#Semimajor and semiminor distances of planet's and comet's orbit are in AU
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

fig=plt.figure()
ax=plt.axes(xlim=(-20.2, 20.2), ylim=(-20.2,20.2))
mercury, =ax.plot([], [],marker='o',markersize=3.25, markerfacecolor= 'fuchsia', label='Mercury')
mercury_o, =ax.plot([],[],color='y',lw=1.5)
venus, =ax.plot([], [],marker='o',markersize=3.5,markerfacecolor='gold', label='Venus')
venus_o, =ax.plot([],[],color='y',lw=1.5)
earth, =ax.plot([], [],marker='o',markersize= 4,markerfacecolor='dodgerblue',label='Earth')
earth_o, =ax.plot([],[],color='y',lw=1.5)
mars, =ax.plot([], [],marker='o',markersize=3.75,markerfacecolor='hotpink',label='Mars')
mars_o, =ax.plot([],[],color='y')
jupiter, =ax.plot([], [],marker='o',markersize= 6, markerfacecolor='lightpink',label='Jupiter')
jupiter_o, =ax.plot([],[],color='y')
saturn, =ax.plot([], [],marker='o',markersize=5.5,markerfacecolor='cyan', label='Saturn')
saturn_o, =ax.plot([],[],color='y')
uranus, =ax.plot([], [],marker='o',markersize=5,markerfacecolor='darkorange', label='Uranus')
uranus_o, =ax.plot([],[],color='y')
#neptune, =ax.plot([], [],marker='o',markersize=6.8, markerfacecolor='white', label='Neptune')
#neptune_o, =ax.plot([],[],color='y')
halley, = ax.plot([],[], marker='o',markersize= 5, markerfacecolor="lime",label='Halley')
halley_o, = ax.plot([],[],color='y')

t=np.linspace(0,2*np.pi, 361)
x1=p1_a*np.cos(t)-p1_a*p1_e
y1=p1_b*np.sin(t)
x2=p2_a*np.cos(t)-p2_a*p2_e
y2=p2_b*np.sin(t)
x3=p3_a*np.cos(t)-p3_a*p3_e
y3=p3_b*np.sin(t)
x4=p4_a*np.cos(t)-p4_a*p4_e
y4=p4_b*np.sin(t)
x5=p5_a*np.cos(t)-p5_a*p5_e
y5=p5_b*np.sin(t)
x6=p6_a*np.cos(t)-p6_a*p6_e
y6=p6_b*np.sin(t)
x7=p7_a*np.cos(t)-p7_a*p7_e
y7=p7_b*np.sin(t)
# x8=p8_a*np.cos(t)-p8_a*p8_e
# y8=p8_b*np.sin(t)
x9=HC_a*np.cos(t)-HC_a*HC_e
y9=HC_b*np.sin(t)

def solar_system(i):
  mercury.set_data(x1[i],y1[i])
  mercury_o.set_data(x1[:i],y1[:i])
  venus.set_data(x2[i],y2[i])
  venus_o.set_data(x2[:i],y2[:i])
  earth.set_data(x3[i],y3[i])
  earth_o.set_data(x3[:i],y3[:i])
  mars.set_data(x4[i],y4[i])
  mars_o.set_data(x4[:i],y4[:i])
  jupiter.set_data(x5[i],y5[i])
  jupiter_o.set_data(x5[:i],y5[:i])
  saturn.set_data(x6[i],y6[i])
  saturn_o.set_data(x6[:i],y6[:i])
  uranus.set_data(x7[i],y7[i])
  uranus_o.set_data(x7[:i],y7[:i])
  # neptune.set_data(x8[i],y8[i])
  # neptune_o.set_data(x8[:i],y8[:i])
  halley.set_data(x9[i],y9[i])
  halley_o.set_data(x9[:i],y9[:i])
  return mercury, mercury_o, venus, venus_o, earth, earth_o, mars, mars_o,jupiter, jupiter_o, saturn, saturn_o, uranus, uranus_o, halley, halley_o, #neptune, neptune_o, 
  
anim=animation.FuncAnimation(fig, solar_system, frames = len(t), interval=25, blit=True, repeat =True)
fig.patch.set_facecolor('k')
fig.tight_layout()
plt.plot(p1_a*p1_e,0,'ro',markersize=6.5, label='Sun')
plt.axis(False)
plt.legend()
"""
plt.rcParams["animation.ffmpeg_path"]= r'C:/ffmpeg/bin/ffmpeg.exe' 
writervideo = animation.FFMpegWriter(fps=20, metadata={"Artist":"Rishikesh Jha"},bitrate=50000) 
anim.save("Intermediate_Solar_System.mp4", writer=writervideo)
"""
plt.show()


