def isprime(p):
    if p>1:
        for i in range(2,int(p**0.5)+1):
            if p%i==0:
                break
        else:
            return 1
    else:
        return 1
n=int(input())
n1=int(input())
c=n+n1
c1=1
while 1:
    c=c+1
    if isprime(c):
        break
    else:
        c1+=1
print(c1)
        
    