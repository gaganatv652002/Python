def factorial(n):
    if n<1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter the number:"))
factorial(n)


output:
Enter the number:5
120
