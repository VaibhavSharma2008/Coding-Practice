from array import array
array1=array("i",[1,4,2,5,7,8,3,4,44,32,3,112,0])
print(array1)
array.reverse(array1)
print(array1)
a=array1[0]
indexing=-1
for i in range(len(array1)):
    indexing+=1
    for j in range(array1.index(a),len(array1)):
        if i>j:
            array1.insert(i,j)
            a=j
            break
print(array1)