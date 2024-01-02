b=[]
n=int(input('Enter number:'))
for i in range(n):
    ele=input('Enter element:')
    b.append(ele)
print(b)
a=str(b)
count=0   
for i in a:
    if i=='a':
        count=count+1
print('Count of a is',count)
