n=input()
a=["a","e","i","o","u"]
for i in n:
    if i in a:
        a.remove(i)
if(len(a)==0):
    print(True)
else:
    print(False)