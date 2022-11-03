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
while True:
    a=a+1
    if (str(a)==str(a)[::-1]):
        if isprime(a):
            print(a)
            break
    