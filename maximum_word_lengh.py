s=input()
l=list(s.split())
a=[]
for i in l:
    a.append(len(i))
print(max(a))