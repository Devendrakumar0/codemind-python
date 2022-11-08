n=input()
mi=n[0]
ma=n[0]
for i in n:
    if(i!=" "):
        if(ord(mi)>ord(i)):
            mi=i
        if(ord(ma)<ord(i)):
            ma=i
print(mi,n.count(mi),ma,n.count(ma))