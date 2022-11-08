n=input()
a="a e i o u"
b=list(a.split())
for i in n:
    if i in b:
        b.remove(i)
if(len(b)==0):
    print(0)
else:
    print(*b)