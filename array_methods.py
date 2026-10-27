import array

array1=array.array("b",[1,1,2,3,4,5,6])
array1.append(9)

print(array1)

array1.insert(3,32)

print(array1)

print("occurence of 1 in the given array is")

print(array1.count(1))

print("adding 999 at index 1 usind insert method")
array1.insert(0,999)
print(array1)

