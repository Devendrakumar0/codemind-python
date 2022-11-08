def vow(p):
    c=0
    for i in p:
        if i in "AEIOUaeiou":
            c+=1
    return(c)

n=input()
l=list(n.split())
a=[]
a=l[0]

for i in l:
    if(vow(a)<vow(i)):
        a=i
print(vow(a))