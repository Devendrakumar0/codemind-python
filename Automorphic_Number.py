n=input()
a=int(n)*int(n)
b=str(a)
if(b.endswith(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")