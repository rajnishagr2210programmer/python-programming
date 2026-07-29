n = int(input("enter a number"))

flag =0
for j in range (2,(n//2)+1):
      if n%j==0:
       flag = 1

if flag==0:
      print(n,"is prime number")
else:
       print(n,"is composite")
