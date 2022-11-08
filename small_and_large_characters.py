n=input()
l=list(n.split())
for i in l:
    mi=i[0]
    ma=i[0]
    for j in i:
        if(ord(mi)>ord(j)):
            mi=j
        if(ord(ma)<ord(j)):
            ma=j
    print(mi,ma,end=" ")