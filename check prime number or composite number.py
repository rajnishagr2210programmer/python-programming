while True :
 n= int(input("enter the number"))
 flag =0
 for i in range (2,(n//2),+1):
     for i in range (1,100):
      if n%i==0:
       flag = 1

 if flag==0:
    print(n,"is prime number")
 else:
    print(n,"is composite")
