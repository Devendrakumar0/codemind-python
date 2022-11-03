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
k=0
for i in range(2,n+1):
    for j in range(2,n+1):
        if i*j==n:
            if isprime(i) and isprime(j):
                print(i,j)
                k+=1
                break
    if k==1:
        break
else:
    print(-1)
        

    
    