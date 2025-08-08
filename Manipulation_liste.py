import numpy as np
def f(x):
  return np.sin(x)-x

N=2à
x1=[]
y1=[]
xmin=10
xmax=30
pas=[xmax-xmin)/(N-1)
for i in range(N):
  x1.append(xmin+i*pas)
  y1.append(f(x1[i])

print("Liste x1:",x1)
print("Liste y2:",y2)
