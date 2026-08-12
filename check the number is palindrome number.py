n=int(input("enter a number"))
num=n
count=0
while n>0:
    n=n//10
    count+=1
n=num
plain=0
while n>0:
    r=n%10
    count=count-1
    plain=plain+(10**count)*r
    n=n//10
if num==plain:
    print(num,"is palindrome")
else:
    print(num,"is not palindrome")

