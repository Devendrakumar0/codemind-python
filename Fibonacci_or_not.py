n=int(input())
a=0
b=1
c=a+b
for i in range(1,n+1):
    a=b
    b=c
    c=a+b
    if c==n:
        print("True")
        break
else:
    print("False")