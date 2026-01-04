print("to check exam is cleared or not")
a=int(input("enter the marks of pre exam: "))
if(a>=100):
    print("pre exam is cleared")
    b=int(input("enter the marks of main exam"))
    if(b>=80):
        print("main exam is cleared")
        c=int(input("enter the marks of interview"))
        if(c>=80):
            print("succesfully selected")
        else:
            print("not selected for interview")
    else:
        print("main exam is not cleared")
else:
    print("pre exam is not cleared")        