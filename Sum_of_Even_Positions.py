n=int(input())
li=list(map(int,input().split()))
sum=0
for i in range(len(li)):
    if i%2==0:
        sum=sum+li[i]
print(sum)
        