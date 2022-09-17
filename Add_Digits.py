n=int(input())
sum=0
while n>0:
    r=n%10
    sum=sum+r
    if sum not in ['0','1','2','3','4','5'
    '6','7','8','9']:
        a=sum%10
        b=sum//10
        sum=a+b
    n=n//10
print(sum)
    
    