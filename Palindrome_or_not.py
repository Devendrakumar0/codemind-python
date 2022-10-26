n=input()
if(n.casefold()==n[::-1].casefold()):
    print(True)
else:
    print(False)