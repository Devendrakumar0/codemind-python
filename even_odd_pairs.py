n=int(input()) 
l=list(map(int,input().split())) 
e=[] 
o=[] 
eo=[] 
for i in l: 
    if(i%2==0): 
        e.append(i) 
    else: 
        o.append(i) 
for i in range(min(len(e),len(o))): 
    eo.append(e[i]) 
    eo.append(o[i]) 
for i in range(min(len(e),len(o)),max(len(e),len(o))): 
    if(len(e)<len(o)): 
        eo.append(o[i]) 
    else: 
        eo.append(e[i]) 
if(len(eo)%2==0): 
    print(*eo) 
else: 
    eo.append(0) 
    print(*eo)