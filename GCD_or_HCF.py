def gcd(a,b):
    if(a==0):
        return(b)
    else:
        if(a<b):
            a,b=b,a
        return(gcd(a%b,b))
a,b=map(int,input().split())
print(gcd(a,b))