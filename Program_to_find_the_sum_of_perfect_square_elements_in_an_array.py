n=int(input())
li=list(map(int,input().split()))
sum=0
for i in li:
    a=int(i**0.5)
    if i==a*a:
        sum=sum+i
print(sum)