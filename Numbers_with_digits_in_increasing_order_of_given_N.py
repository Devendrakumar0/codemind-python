def i_d(N):
  if N == 1:
    for i in range(10):
      print(i,end=" ")
  else:
    for i in range(1, 10):
      idh(N-1, str(i))

def idh(N,x):
  if N == 0:
    print(x,end=" ")
  else:
    for i in range(int(x[-1])+1, 10):
      idh(N-1, x+str(i))

N = int(input())
i_d(N)
