for i in range(0,6):
    for j in range(0,6):
        print(j,end=" ")
    print( )

for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=(" "))
    print( )


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print( )

for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print()  

for i in range(1,6):
    for j in range(i,6):
        print("*",end=" ")
    print()

for a in range(5,0,-1):
    for b in range(6-a,6):
        print("*",end=" ")  
    print()

for a in range(5,0,-1):
    for b in range(6-a,6):
        print(b,end=" ")  
    print()

a=input("enter your name:")
b=len(a)
for i in range(0,b):
    for j in range(0,i+1):
        print(a[j],end=" ")
    print()
