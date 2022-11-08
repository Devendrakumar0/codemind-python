n=input()
a=[]
for i in n:
    if i in "AEIOUaeiou":
        if i not in a:
            a.append(i)
print(*a)