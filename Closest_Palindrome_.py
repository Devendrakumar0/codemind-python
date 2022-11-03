n=int(input())
a=str(n)
b=n-1
c=n+1
while True:
    b1=str(b)
    if b1[::-1]==b1:
        d=abs(b-n)
        break
    else:
        b=b-1
while True:
    c1=str(c)
    if c1[::-1]==c1:
        d1=abs(c-n)
        break
    else:
        c=c+1
if d>d1:
    print(c)
elif d1>d:
    print(b)
else:
    print(b,c)
        
        