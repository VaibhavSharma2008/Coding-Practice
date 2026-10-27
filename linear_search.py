test=[5, 2, 8, 1, 3]
def search_fun():
    try:
        search=int(input("enter number to search: "))
        for number in range(len(test)):
            if test[number]==search:
                print(f"{test[number]} and index {number}")
                search_fun()
    except KeyboardInterrupt:
        pass
search_fun()
