n=int(input())
li=list(map(int,input().split()))
avg=(sum(li))/n
print("{:.2f}".format(avg))