#lecture 2 
a=int(input("enter the no. of which you want to find the table:"))
for j in range(0,11):
    print(a,"*",j,"=",a*j)
print("to find the division of it")
for i in range(1,10):
    c=a/i
    print(a,"/",i,c)
print("to enter the modulus of given no. ")
for k in range(1,10):
    d=a%k
    print(a,"%",k,d)
#to print the sum of 1 to 100 numbers 
sum=0
for h in range(1,101):
    sum=sum+h
print("sum of numbers are",sum)
m=int(input("entyer the no. to find factorial:"))
fact=1
for z in range(m,1,-1):
    fact=fact*z
print(fact)
