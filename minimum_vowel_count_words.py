def vow(p):
    c=0
    for i in p:
        if i in "AEIOUaeiou":
            c+=1
    return(c)

n=input()
l=list(n.split())
a=[]
for i in l:
    a.append(vow(i))
print(a.count(min(a)))
    