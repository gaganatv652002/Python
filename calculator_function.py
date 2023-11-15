def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
print("1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplication\n"
      "4.Division")
ch=int(input("Enter the choice:"))
print("result is:")
if ch==1:
    print(num1+num2)
elif ch==2:
    print(num1-num2)
elif ch==3:
    print(num1*num2)
else:
    print(num1/num2)


output:
Enter the first number:5
Enter the second number:5
1.Addition
2.Subtraction
3.Multiplication
4.Division
Enter the choice:3
Result is:
25
