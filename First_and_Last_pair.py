n=int(input()) 
l=list(map(int,input().split()))
a=len(l)
for i in range(len(l)//2):
    print(l[i],l[a-i-1],end=" ")
if(a%2!=0):
    print(l[a//2],0)