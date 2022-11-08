n=input()
l=list(n.split())
mi=l[0][0]
ma=l[0][0]
for i in l[0]:
    if(ord(mi)>ord(i)):
        mi=i
print(mi,end=" ")
mi=l[-1][0]
ma=l[-1][0]
for i in l[-1]:
    if(ord(ma)<ord(i)):
        ma=i
print(ma,end=" ")
    