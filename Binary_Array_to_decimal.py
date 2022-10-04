n=int(input())
test_list=list(map(int,input().split()))
res=0
j=0
for i in range(len(test_list),0,-1):
	x=2**j
	res+=x*test_list[i-1]
	if(j>len(test_list)):
		break
	j+=1
print (str(res))
