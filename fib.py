user=int(input("enter a number: "))
a=0
b=1
print(a,b,sep="\n")
for i in range(2,user):
    print(a+b)
    a,b=b,a+b
