for _ in range(int(input())):
    a=input()
    a=sorted(a)
    for i in range(len(a)-1):
        if(abs(int(a[i])-int(a[i+1]))!=1):
            print("NO")
            break
    else:
        print("YES")