def palin(p):
    if(p==p[::-1]):
        return(1)
    else:
        return(0)
n=input()
c=0
a=list(n.split(" "))
for i in a:
    if(palin(i.casefold())==1):
        c+=1
print(c)