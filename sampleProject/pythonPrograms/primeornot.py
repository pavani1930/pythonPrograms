n=int(input("Enter a number"))
count=0
for i in range(2,n):
    if (n%i==0):
        count=count+1
if count==2:
    print("Prime number")
else:
    print("Not a prime number")