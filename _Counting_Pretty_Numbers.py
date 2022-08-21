n=int(input())
for i in range(n):
    a=["2","3","9"]
    c=0
    l,r=input().split()
    for j in range (int(l),int(r)+1):
        j=str(j)
        if j[-1] in a:
            c+=1
    print(c)

        
        
