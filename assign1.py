"""WAP STORES NAME,AGE,AND WEATHER YOU ARE STUDENT IN SEPARATE VARIABLES PRINT THEM WITH CLEAR LABELS"""
a=input("enter name:")
b=int(input("enter age:"))
c=bool(input("are you student:"))
print("name is:",a)
print("age is:",b)
print("are you student:",c)
if c==True:
    e=input("enter your school/college name:")
    d=int(input("enter your roll number:"))
    f=[]
    f.append(a)
    f.append(b)
    f.append(c)
    f.append(e)
    f.append(d)
    print(f)
else:
    print("ok")
