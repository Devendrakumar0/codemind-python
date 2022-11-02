n=int(input())
for i in range(1,n//2):
    if(n%i==0):
        if(abs(i-(n/i))==1):
            print("YES")
            break
else:
    print("NO")
        