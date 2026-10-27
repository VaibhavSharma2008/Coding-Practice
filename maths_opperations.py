operation=input("""
            OPERATIONS:-
                -SUM (+)
                -SUBSTRATION(-)
                -MULTIPLICATION(*)
                -DIVISION(/)
                -EXPONENT(**)
                -FLOOR DIVISION(//)
enter opperation: """).strip().replace(" ","")
x=float(input("enter a number: "))
y=float(input("enter a number: "))
if operation=="+":
    solution=x+y
    print(f"addition is {solution}")
if operation=="-":
    solution=x-y
    print(f"subtraction is {solution}")
if operation=="*":
    solution=x*y
    print(f"multiplication is {solution}")
if operation=="/":
    solution=x/y
    print(f"division is {solution}")
if operation=="**":
    solution=x**y
    print(f"exponential is {solution}")
if operation=="//":
    solution=x//y
    print(f"floor division is {solution}")