a=int(input("enter the first number:"))
b=int(input("enter the first number:"))
try:
    c=a/b
    print("Result:",c)
except:
    print("Can't divide by zero")
else:
    print("Done")

output:
enter the first number:5
enter the first number:1
Result: 5.0
Done
