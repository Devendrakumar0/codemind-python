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
a=str(n)
b=str(n)[::-1]
a=int(a)
b=int(b)
if isprime(a):
    if isprime(b):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")