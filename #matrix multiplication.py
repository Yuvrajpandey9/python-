#matrix multiplication 
a=[[]]
b=[[]]
p=[[]]
r=int(input("enter the no. of rows:"))
c=int(input("enter the no. of coloumns:"))
print("enter the details of 1 matrix:")
for i in range(r):
    a.append([ ])
for i in range(r):
    for j in range(c):
        val=int(input("enter the values of list"))
        a[i].append(val)
print("please enter the values of 2 list")
for i in range(r):
    b.append([ ])
for i in range(r):
    for j in range(c):
        val=int(input("enter the values of list"))
        b[i].append(val)

#multiplication
for i in range(r):
    for j in range(c):
        for k in range(r):
            p[i][j]=p[i][j]+a[k][j]*b[i][k]
print (p)

