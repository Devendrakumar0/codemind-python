def prime(i):
    if(i>1):
        for j in range(2,int(i**(0.5))+1):
            if(i%j==0):
                return(0)
        else:
            return(1)
    else:
        return(0)

n=int(input())
a=(str(n)[::-1])
n1=int(a)
if(prime(n)):
    if(prime(n1)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")