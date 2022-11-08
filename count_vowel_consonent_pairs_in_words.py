def che(a):
    d=int(len(a)/2)
    c=0
    for i in range(d):
        if((a[i] in "aeiouAEIOU")and(a[len(a)-i-1] not in "aeiouAEIOU")):
            c+=1
        elif((a[i] not in "aeiouAEIOU") and (a[len(a)-i-1] in "aeiouAEIOU")):
            c+=1
    return(c)
n=input()
l=list(n.split())
c=0
for i in l:
    c+=che(i)
print(c)