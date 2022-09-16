n=int(input())
li=list(map(int,input().split()))
half=len(li)//2
l1=li[:half]
l2=li[half:]
l2=l2[::-1]
l3=l2+l1
res = str(l3)[1:-1]
print(res.replace(",",""))