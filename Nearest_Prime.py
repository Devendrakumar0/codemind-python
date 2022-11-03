def isprime(p):
    if p>1:
        for i in range(2,int(p**0.5)+1):
            if p%i==0:
                break
        else:
            return 1
    else:
        return 1
for _ in range(int(input())):
    a=int(input())
    b=a
    c=a
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
    if d>d1:
        print(c)
    elif d1>d:
        print(b)
    else:
        print(min(b,c))
    
