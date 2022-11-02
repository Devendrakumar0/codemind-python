n=input()
n1=n[::-1]
a=int(n)
s=a*a
s1=str(s)[::-1]
for i in range(len(n)):
    if(s1[i]!=n1[i]):
        print("Not an Automorphic Number")
        break
else:
    print("Automorphic Number")