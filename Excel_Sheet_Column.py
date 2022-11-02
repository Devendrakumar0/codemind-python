n=int(input())
s=""
while(n>0):
    r=((n-1)%26)+65
    s=chr(r)+s
    n=(n-1)//26
print(s)