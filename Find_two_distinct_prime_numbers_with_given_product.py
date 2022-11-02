n=int(input())
def prime(i):
    if(i>1):
        for j in range(2,int(i**(0.5))+1):
            if(i%j==0):
                return(0)
        else:
            return(1)
    else:
        return(0)
for i in range(1,int(n**(0.5))+1):
    if(n%i==0 and prime(i)):
        if(prime(n//i)):
            print(i,n//i)
            break
else:
    print(-1)
        