test=[5, 2, 8, 1, 3]
for number in range(len(test)-1):
    for number in range(len(test)-1):
        if test[number]>test[number+1]:
            test[number],test[number+1]=test[number+1],test[number]
print(test)