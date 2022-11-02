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
    while(n>0):
        r=n%10
        if(prime(r)==0):
            print("Not Mega Prime")
            break
        n=n//10
    else:
        print("Mega Prime")
else:
    print("Not Mega Prime")