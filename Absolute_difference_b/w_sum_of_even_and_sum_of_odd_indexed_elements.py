n=int(input())
li=list(map(int,input().split()))
sum1=sum2=0
for i in range(len(li)):
    if i%2==0:
        sum1=sum1+li[i]
    else:
        sum2=sum2+li[i]
print(abs(sum1-sum2))