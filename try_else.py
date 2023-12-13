try:
    a=int(input("Enter a:"))
    b=int(input("enter b:"))
    c=a/b
    print("a/b=",c)
except Exception:
    print("Cant divide by zero")
    print("Exception")
else:
    print("Hii I'am else block")

output:-
Enter a:4
enter b:2
a/b= 2.0
Hii I'am else block
