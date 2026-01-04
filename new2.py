a=int(input("enter the number"))
b=int(input("enter the second number "))
if (a==b):
    print("the number is eqaul")
    c=a*b
    print("sqauare of these two numbers is equal to multipliacation of these two number",c)
elif (a>b):
    d=a/b
    print("hence the number is smaller hence the division of these two numbers is",d)
else:
    print("no. is equal")
    print("create a matrix to solve")
    f=[[]]
    h=[[]]
    print("enter the details of 1 matrix:")
    e=int(input("enter the rows of matrix"))
    g=int(input("enter the coloumn of matrix"))

    for i in range(e):
        a.append([ ])
    for i in range(e):
        for j in range(g):
            val=int(input("enter the values of list"))
            a[i].append(val)
    h[[]]=f*f
    print("square of a matrix is",h)
