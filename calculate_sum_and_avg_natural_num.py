first_n=int(input("enter a number: "))
sum=float()
for i in range(first_n+1):
    sum+=i
average=sum/first_n
print(f"average is {average}")
print(f"sum is {sum}")