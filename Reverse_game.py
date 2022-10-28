n=int(input())
s=input()
l=s.split(" ")
for i in l:
    print(int(i[::-1]),end=" ")
    