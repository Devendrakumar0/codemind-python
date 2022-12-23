n=int(input())
li=[]
for i in range(n):
    li.append("x")
for i in range(n):
    li[i]="0"
    for j in li:
        print(j,end="")
    li[i]="x"
    print("")