n=int(input())
a=0
b=1
c=a+b
for i in range(1,n+1):
    a=b
    b=c
    c=a+b
    if abs(b-n)<abs(c-n):
        print(b)
        break
    elif abs(b-n)>abs(c-n):
        continue
    else:
        print(b,c)
        break