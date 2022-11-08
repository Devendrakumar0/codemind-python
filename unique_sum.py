n=int(input()) 
l=list(map(int,input().split()))
s=0
a=[]
for i in l:
    if(i not in a):
        s+=i
        a.append(i)
print(s)