a=input()
c=0
for i in range(int(len(a)/2)):
    if(a[i]==" " or a[len(a)-i-1]==" "):
        continue
    else:
        if((a[i] in "aeiouAEIOU")and(a[len(a)-i-1] not in "aeiouAEIOU")):
            c+=1
        elif((a[i] not in "aeiouAEIOU") and (a[len(a)-i-1] in "aeiouAEIOU")):
            c+=1
print(c)