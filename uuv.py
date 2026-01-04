def test(N):
    s=0
    for i in range(1,N):
        if(N%i==0):
            s=s+i
    if(s==N):
        print("given no. is a perfect no.")
    else:
        print("given no. is not a perfect no.")

#main program
N=int(input("enter the no."))
test(N)

