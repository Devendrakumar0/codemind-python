def isprime(p):
    if p>1:
        for i in range(2,int(p**0.5)+1):
            if p%i==0:
                break
        else:
            return 1
    else:
        return 0
n=int(input())
f=False
if isprime(n):
    a=str(n)
    for i in a:
        if isprime(int(i)):
            f=True
        else:
            f=False
            break
    if f:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")