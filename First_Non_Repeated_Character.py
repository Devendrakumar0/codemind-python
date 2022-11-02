for _ in range(int(input())):
    n=int(input())
    s=input()
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    a=[]
    for k,v in d.items():
        if(v==1):
            a.append(k)
    for i in s:
        if(i in a):
            print(i)
            break
    else:
        print(-1)