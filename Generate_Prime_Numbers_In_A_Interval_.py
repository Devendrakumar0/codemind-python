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
for j in range(n,n1+1):
    if j>1:
        if isprime(j):
            print(j)