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
c=0
a=l.index(min(l))
b=l.index(max(l))
if(a<b):
    for i in range(a,b+1):
        if(prime(l[i])==1):
            c+=1
else:
    for i in range(b,a+1):
        if(prime(l[i])==1):
            c+=1
print(c)