def linear_searching(a,n):
    N=len(a)
    for i in range(0,N):
        if a[i]==n:
            print("no. found at",i)
#main program
a=eval(input("enter the elements of list:"))
n=int(input("enter the no. u want to find"))
linear_searching(a,n)
