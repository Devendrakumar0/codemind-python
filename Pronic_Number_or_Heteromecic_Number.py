n=int(input())
for i in range(1,int(n**(0.5))+1):
    if(n%i==0):
        if(n//i == i+1):
            print("YES")
            break
else:
    print("NO")