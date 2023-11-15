def fibonacci(n):
    if(n<=1):
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
n=int(input("Enter the term:"))
if(n<=0):
    print("Enter positive number")
else:
    print("fibonacci sequence:")
    for i in range(n):
        print(fibonacci(i))

output:
Enter the term:5
fibonacci sequence:
0
1
1
2
3
