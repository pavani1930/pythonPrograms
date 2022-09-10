def fibonacci(n):
    if n<0:
        print("please enter a valid number")
    elif n==0:
        return n 
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter a number"))
result=fibonacci(n)
print(result)
        