n=int(input())
sum=0
for i in range(1,n+1):
    a=1/i
    sum=sum+a
print("{:.2f}".format(sum))