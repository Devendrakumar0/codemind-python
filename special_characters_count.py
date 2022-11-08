n=input()
c=0
for i in n:
    if(i.isalnum()==False and i!=" "):
        c+=1
print(c)