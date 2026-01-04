#canteen menu system 
"""coldrink-pepsi 30 rupees,coke 40 rupees,maaza-50 rupees snack chips-samosa 40 rupees,patees 40 rupees,burger 50 rupees and exit and also add quantity and hence represent the final bill"""
print("MENU snacks and cold drinks available:")
sum=0
while True:
    c=input("enter your choice:(yes/no)")
    if(c=="yes"):
        a=int(input("press 1 for cold drink and 9 for snacks:"))
        if (a==1):
            print("coke-40" \
            "pepsi-30" \
            "maza-50")
            print("2 for coke:")
            print("3 FOR MAZA:")
            print("4 for pepsi:")
            b=int(input("enter your choice:"))
            q=int(input("enter the quantity:"))
            if (b==2):
                sum=sum+40*q
            elif (b==3):
                sum=sum+50*q
            elif(b==4):
                sum=sum+30*q
            else:
                print("correct your choice!!")
        elif(a==9):
            print("burger=50" \
            "patties=40 rupees" \
            "samosa=40" \
            "popcorn=70")
            print("5 for burger,6 for patties,7 for samosa and 8 for popcorn")
            d=int(input("enter your choice:"))
            q=int(input("enter the quantity:"))
            if(d==5):
                sum=sum+50*q
            elif (d==6):
                sum=sum+40*q
            elif (d==7):
                sum=sum+40*q
            elif (d==8):
                sum=sum+70*q
            else:
                print("correct your choice!!")

        else:
            print("correct your choice!!")
    elif(c=="no"):
        break
    else:
        print("wrong input as pyhton is case sensitive!!!")
print("your final bill is:",sum)
print("thank you visit again :)")
        
