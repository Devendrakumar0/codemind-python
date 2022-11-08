n=int(input()) 
l=list(map(int,input().split()))
print(*l,end=" ")
if(len(l)%2!=0):
    print(0)