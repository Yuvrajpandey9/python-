a=[[]]
b=[[]]
c=[[]]
import numpy as np
r=int(input("enter the rows"))
c=int(input("enter the coloumns"))
p=np.zeros(r,c)
print("enter the details of 1 list:")
for i in range(r):
    a.append([])
    for i in range(r):
        for j in range(c):
            val=int(input(""))
            a[i]=append(val)
print("now please enter the details of 2 list:")
for i in range(r):
    a.append([])
    for i in range(r):
        for j in range(c):
            val=int(input(""))
            b[i].append(val)
            

for i in range(r):
    for j in range(c):
        for k in range(r):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]

print("product matrix is")
for i in range(r):
    for j in range(c):
        print(c[i][j],end='')
print()
