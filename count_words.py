n=input()
c=0
l=list(n.split())
for i in l:
    if(i[0] in "AEIOUaeiou")and(i[-1] not in "AEIOUaeiou"):
        c+=1
print(c)