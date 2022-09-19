n=int(input())
a=n*n
sum=0
t=a
while a>0:
    r=a%10
    sum=sum+r
    a=a//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")
    