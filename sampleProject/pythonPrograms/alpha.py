n=int(input())
num=65
for i in range(n):
    for j in range(i+1):
        print(chr(num+i),end=" ")
        num=num+1
    print()