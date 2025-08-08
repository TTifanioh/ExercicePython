import matplotlib.pyplot as plt
import math
def f1(x):
  if x>=0 and x<1 :
    return x
  elif x>=1 and x<=2 :
    return 1

def f2(x):
  return math.sin(x)+0.1

xmin=0
xmax=2
pas=0.05
N=int(((xmax-xmin)/pas)+1)
x=[]
y1=[]
y2=[]
for i in range(N):
  x.append(i*pas)
  y1.append(f1(x[i])
  y2.append(f2(x[i])

plt.figure()
plt.plot(x,y1,color='blue',linewidth=3)
plt.plot(x,y2,color='red',marker='*')
plt.legend(['Fonction courbe 1','Fonction courbe 2'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Tracé des courbes')
plt.axis([0,2,0,1.5])
plt.show()  
