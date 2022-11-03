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
a=n
b=n
c=n
if isprime(a):
    print(0)
else:
    while 1:
        if isprime(b):
            break
        else:
            b=b-1
    while 1:
        if isprime(c):
            break
        else:
            c=c+1
    d=abs(b-a)
    d1=abs(c-a)
    print(min(d,d1))
    