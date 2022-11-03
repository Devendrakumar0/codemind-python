def checkDivisibility(n, digit) :
	return (digit != 0 and n % digit == 0)
def allDigitsDivide( n) :
	temp = n
	while (temp > 0) :
		digit = temp % 10
		if ((checkDivisibility(n, digit)) == False) :
			return False
		temp = temp // 10
	return True
n=int(input())
n1=int(input())
for i in range(n,n1+1):
    if allDigitsDivide(i):
        print(i,end=" ")
