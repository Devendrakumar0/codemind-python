a,b=map(int,input().split())
li=[]
li1=[]
for i in range(a,10000):
    if i%a==0:
        li.append(i)
for j in range(b,10000):
    if j%b==0:
        li1.append(j)
print(min(set(li) & set(li1)))
        
