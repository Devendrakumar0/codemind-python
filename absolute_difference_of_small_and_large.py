def mine(s):
    mi=s[0]
    ma=s[0]
    for i in s:
        if(ord(mi)>ord(i)):
            mi=i
        if(ord(ma)<ord(i)):
            ma=i
    print(abs(ord(mi)-ord(ma)),end=" ")
n=input()
l=list(n.split())
for i in l:
    mine(i)
    