from vpython import *
#GlowScript 3.1 VPython
scene.width = 750
scene.height = 530
scene.range = 1.1
scene.background = vector(0.9,0.9,0.9)
scene.align = "right"

    
scene.caption = "<b>Effect of Stiffness on Time Period  </b>\n\n\n"
square=box(pos=vector(0,-1,0),velocity=vector(0,0.7,0),size=vector(1.27,1,1.2),color=vec(0,0,0.4),mass=2, force=vector(0,0,0))
pivot=vector(0,4,0)
spring=helix(pos=pivot, axis=square.pos-pivot, radius=0.4, constant=1, thickness=0.1, coils=15, color=color.red,stiffness=120)
wall=box(pos=pivot,size=vector(3,0.2,3),color=color.green)


# mass input
def m(x):
 print (x.number)
m=winput(bind=m,width=130, prompt=" Enter mass(m):       ",type="numeric")
wtext(text=" kg")
scene.append_to_caption('\n\n\n')

#Stiffness input
def k(y):
 print (y.number)
k=winput(bind=k,width=130,prompt=" Enter Stiffness(k):   ",type="numeric")
wtext(text=" N/m")
scene.append_to_caption('\n\n')

#Calculate TimePeriod   
def calculate(y,x):
 T=2*3.14/sqrt(y/x)
 return T
 
def pt(y,x):
 print (calculate(2,120))

button(bind=pt ,text ="<b>  Calculate  </b>",color=color.white,background=color.blue)

eq_pos = spring.pos+spring.axis

t=0
dt = 0.01
while (t<50):
    rate(100)
    square.force = -spring.stiffness*(square.pos-eq_pos)
    square.velocity = square.velocity + square.force/square.mass*dt
    square.pos = square.pos + square.velocity*dt
    spring.axis = square.pos-spring.pos
    t=t+dt






  
      
