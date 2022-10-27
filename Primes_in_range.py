def isprime(p):
    if p<=1:
        return 0
    else:
        for i in range(2,int(p**0.5)+1):
            if p%i==0:
                return 0
        else:
            return 1
n=int(input())
n1=int(input())
c=0
for j in range(n,n1+1):
    if(isprime(j)==1):
        c+=1
print(c)
        