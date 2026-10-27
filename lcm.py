num1=int(input("enter a number: "))
num2=int(input("enter second number: "))
if num1>num2:
    greatest=num1
else:
    greatest=num2
condition=True
while condition:
    if (greatest%num1==0) and (greatest%num2==0):
        lcm=greatest
        condition=False
    else:
        greatest+=1
print(lcm)