test=[1, 2, 3, 4, 5]
search=int(input("enter a number to search: "))
indexing=(len(test)-1)//2
start=0
end=len(test)-1
while start<=end:
    if test[indexing]>search:
        end=indexing-1
        indexing=(start+end)//2
    elif test[indexing]<search:
        start=indexing+1
        indexing=(start+end)//2
    if test[indexing]==search:
        print(f"found {search} at index {indexing}")
        break
    else:
        print("number doesnt exist in list")
