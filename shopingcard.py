#shoping cart manager
n=int(input("Enter the number of items you want to add in your shopping cart: ")) 
a=[]
stk=[]
print("no. of items in a cart is",n)
for i in range(n):
    item=input("Enter the item you want to add in your shopping cart: ")
    a.append(item)
def isempty(a):
    if(a==[]):
        return True
    else:
        return False

def push(a,item):
    stk.append(item)
    top=len(a)-1

def pop(a):
    if (isempty(a)):
        return("underflow")
    else:
        i=a.pop()
        if(len(a)==0):
            top=None
        else:
            top=top-1
    return(i)

def peak(a):
    if (isempty(a)):
        return("underflow")
    else:
        top=len(a)-1
        return(a[top])

def display(a):
    if (isempty(a)):
        print("stack is empty")
    else:
        top=len(a)-1
        print(a[top],"<-----top")
        for i in range(top-1,-1,-1):
            print(a[i])




#main program
while True:
    print("STACK IMPLEMENTATION")
    print("1.push")
    print("2.pop")
    print("3.peak")
    print("4.display")
    print("5.exit")

    ch=int(input("enter your choice"))
    if (ch==1):
        item=input("enter the no. you want to push:")
        push(a,item)
        print("item added successfully")
    elif (ch==2):
        s=pop(a).s
        if (item=="underflow"):
            print("empty")
        else:
            print("item poped successfully")
    elif (ch==3):
        item=peak(a)
        if (item=="underflow"):
            print("underflow!,stack is empty")
        else:
            print("item is at top")
    elif (ch==4):
        display(a)
    elif (ch==5):
        break
    else:
        print("#andha hai kya lavde# ")
