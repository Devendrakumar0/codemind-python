def prime(p):
    if(p>1):
        for i in range(2,int(p**(0.5))+1):
            if(p%i==0):
                return(0)
                break
        else:
            return(1)
    else:
        return(0)
n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in l:
    if(prime(i)==1):
        s+=i
        c+=1
print("%.2f"%(s/c))