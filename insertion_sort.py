test = [5, 2, 4, 1, 3]

for i in range(1, len(test)):
    current = test[i]
    j = i - 1

    while j >= 0 and test[j] > current:
        test[j + 1] = test[j]
        j -= 1

    test[j + 1] = current

print(test)