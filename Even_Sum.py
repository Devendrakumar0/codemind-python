n=int(input())
li=list(map(int,input().split()))
sum=0
for i in li:
    if i%2==0:
        sum=sum+i
print(sum)