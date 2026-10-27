num1=int(input("enter a number: "))
num2=int(input("enter another number: "))
hcf=num1*num2
condition=True
while condition:
    if (num1%hcf==0) and (num2%hcf==0):
        condition=False
    else:
        hcf-=1
print(hcf) 