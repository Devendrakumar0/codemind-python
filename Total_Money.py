for _ in range(int(input())):
    t=0
    D,i,r,ir=map(int,input().split())
    n=D//i
    k=0
    for j in range(n):
        t+=(i*(r+(k*ir)))
        k+=1
    re=D%i
    t+=(re*(r+(k*ir)))
    print(t)