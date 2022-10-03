n=int(input())
li=list(map(int,input().split()))
sum1=sum2=0
for i in li:
    if (i%2)==0:
        sum1=sum1+i
    else:
        sum2=sum2+i
print(abs(sum1-sum2))