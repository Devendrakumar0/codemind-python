def numSquareSum(n):
 squareSum = 0;
 while(n):
  squareSum += (n % 10) * (n % 10);
  n = int(n / 10);
 return squareSum;
def isHappynumber(n):
 n1 = n;
 n2 = n;
 while(True):
  n1 = numSquareSum(n1);
  n2 = numSquareSum(numSquareSum(n2));
  if(n1!= n2):
   continue;
  else:
   break;
 return (n1 == 1);
n = int(input())
if (isHappynumber(n)):
 print("True");
else:
 print("False");

