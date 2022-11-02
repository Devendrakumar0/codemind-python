n=int(input())
a=0
b=1
c=a+b
if(n==0 or n==1):
    print(True)
else:
    while(c<n):
        c=a+b
        if(c==n):
            print(True)
            break
        else:
            a=b
            b=c
    else:
        print(False)