l=[]
f=r=None

def isempty(l):
    if (l==[]):
        return True
    else:
        return False
def enqueue (l,item):
    l.append(item)
    if (len(l)==1):
        f=r=0
    else:
        r=len(l)-1
def dequeue(l):
    if (isempty(l)):
        return("underflow")
    else:
        i=l.pop(0)
    if (len(l)==0):
        f=r=None
def peak():
    if(isempty(l)):
        return("underflow!")
    else:
        f=0
        return(l(f))
def display():
    if(len(l)==0):
        print("given queue is empty!")
    elif (len(l)==1):
        print(l[0],"<---front<---rear")
    else:
        f=0
        r=len(l)-1
        print(l[f],"<--front")
        for x in range(1,r):
            print(l[x])
        print(l[r],"<==rear")

#main program
while True:
    print("\n\n")
    print("STACK IMPLEMENTATION")
    print("1.enqueue")
    print("2.dequeue")
    print("3.peak")
    print("4.display")
    print("5.exit")

    ch=int(input("enter your choice"))
    if (ch==1):
        item=input("enter the no. you want to push:")
        enqueue(l,item)
        print("item added successfully")
    elif (ch==2):
        item=dequeue(l)
        if (item=="underflow"):
            print("empty")
        else:
            print("item poped successfully")
    elif (ch==3):
        item=peak(l)
        if (item=="underflow"):
            print("underflow!,stack is empty")
        else:
            print("item is at top")
    elif (ch==4):
        display(0)
    elif (ch==5):
        break
    else:
        print("ANDHE 1-5 TAK DENA THA")


        
