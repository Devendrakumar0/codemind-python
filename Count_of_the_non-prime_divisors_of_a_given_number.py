def prime(n):
    if n==1:
        return 1
    elif n==2:
        return 0
    else:
        for i in range(2,(n//2)+1):
            if n%i==0:
                return 1
        else:
            return 0
            
n=int(input())
l=[]
c=1
for i in range(1,n//2+1):
    if n%i==0:
        s=prime(i)
        if(s==1):
            c+=1
print(c)