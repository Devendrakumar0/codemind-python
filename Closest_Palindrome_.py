n=int(input())
b=n
a=n
while(1):
    a=a-1
    if(str(a)==str(a)[::-1]):
        a1=a
        break
while(1):
    n=n+1
    if(str(n)==str(n)[::-1]):
        a2=n
        break
d1=abs(a1-b)
d2=abs(a2-b)
if(d1<d2):
    print(a1)
elif(d1>d2):
    print(a2)
else:
    print(a1,a2)