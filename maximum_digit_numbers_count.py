n=int(input())
l=list(map(int,input().split()))
b=[]
for i in l:
    a=str(i)
    b.append(len(a))
c=max(b)
for i in l:
    if(len(str(i))==c):
        print(i,end=" ")