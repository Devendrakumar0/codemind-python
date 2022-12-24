n=int(input())
li=list(map(int,input().split()))
li1=[]
li2=[]
for i in range(n):
    if i%2!=0:
        li[i-1]=str(li[i-1])
        li1.append(li[i-1]*li[i])
for i in li1:
   for j in i:
       li2.append(j)
print(*li2)
        
        
        