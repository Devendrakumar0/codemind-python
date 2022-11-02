for _ in range(int(input())):
    a=input()
    for i in a:
        if(i.isdigit()!=True):
            print(False)
            break
    else:
        print(True)