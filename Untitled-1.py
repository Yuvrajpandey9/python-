def insertion_sorting(a,n):
    for i in range(1,n):
        t=a[i]
        j=i-1
        while j>=0 and t<a[j]:
            a[j+1]=a[j]
            j=j-1
        else:
            a[j+1]=t
            break
    return(a)
#main program
n=int(input("enter the size of a list:"))
a=[]
for i in range(n):
    val=int(input("enter the values of a list:"))
    a.append(val)
p=insertion_sorting(a,n)
print(p)