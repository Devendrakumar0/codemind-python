n=int(input())
li=list(map(int,input().split()))
max=0
for i in li:
    if i%2==0:
        max=i
print(max)
        