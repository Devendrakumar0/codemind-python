n=input()
l=list(n.split())
a=l[-1]
c=a[0]
for i in a:
    if(ord(i)<ord(c)):
        c=i
if(c.isupper()and(c.lower() in l[-1])):
    print(c.lower())
else:
    print(c)