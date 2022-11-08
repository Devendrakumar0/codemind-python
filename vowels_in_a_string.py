n=input()
a=input()
c=0
for i in n:
    if(i==a):
        print(True)
        print(c)
        break
    else:
        c+=1
else:
    print(False)