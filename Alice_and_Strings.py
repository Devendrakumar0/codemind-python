for _ in range(int(input())):
    s2=input()
    s3=input()
    for i in range(len(s2)):
        if(s2[i]>s3[i]):
            print("NO")
            break
    else:
        print("YES")