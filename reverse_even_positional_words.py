s=input()
l=list(s.split())
for i in range(len(l)):
    if(i%2==0):
        a=l[i]
        print(a[::-1],end=" ")
    else:
        print(l[i],end=" ")