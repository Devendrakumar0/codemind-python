def prime(p):
    if(p>1):
        for i in range(2,int(p**(0.5))+1):
            if(p%i==0):
                return(0)
        else:
            return(1)
    else:
        return(0)

n=int(input())
if(prime(n)):
    print(0)
else:
    i=n-1
    j=n+1
    while(1):
        if(prime(i)):
            d1=abs(i-n)
            break
        else:
            i-=1
    while(1):
        if(prime(j)):
            d2=abs(j-n)
            break
        else:
            j+=1
    print(min(d1,d2))