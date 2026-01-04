s=[]

def isempty(stk):
    if(stk==[]):
        return True
    else:
        return False

def push(stk,item):
    stk.append(item)
    top=len(stk)-1

def pop(stk):
    if (isempty(stk)):
        return("underflow")
    else:
        i=stk.pop()
        if(len(stk)==0):
            top=None
        else:
            top=top-1
    return(i)

def peak(stk):
    if (isempty(stk)):
        return("underflow")
    else:
        top=len(stk)-1
        return(stk[top])

def display(stk):
    if (isempty(stk)):
        print("stack is empty")
    else:
        top=len(stk)-1
        print(stk[top],"<-----top")
        for i in range(top-1,-1,-1):
            print(stk[i])




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
        item=int(input("enter the no. you want to push:"))
        push(s,item)
        print("item added successfully")
    elif (ch==2):
        s=pop(s)
        if (item=="underflow"):
            print("empty")
        else:
            print("item poped successfully")
    elif (ch==3):
        item=peak(s)
        if (item=="underflow"):
            print("underflow!,stack is empty")
        else:
            print("item is at top")
    elif (ch==4):
        display(s)
    elif (ch==5):
        break
    else:
        print("#andha hai kya lavde# ")
