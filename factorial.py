def factorial(num):
    if num>=1:
        solution=1
        while num!=1:
            solution*=num
            num-=1
        print(solution)
    elif num==1:
        print("factorial is 1")
        return num
user=int(input("enter a num for factorial: "))
factorial(user)