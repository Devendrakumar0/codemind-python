s=input()
n=int(input())
c=s.count("a")
d=n//len(s)
ae=d*c
if(n%len(s)!=0):
    su=s[:(n%len(s))]
    ae+=(su.count('a'))
print(ae)