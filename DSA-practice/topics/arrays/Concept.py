import array as arr

array = arr.array('i', [1,2,3,4,5])
print("The new created array is : ")

#prints the array with 'i' as the typecode
print(array) 

# prints each element of the array
for i in range (0, 5):
    print(array[i])

# prints the type of elements of the array
print(array.typecode)

# prints the length of the array
print(len(array))

# prints the buffer information
print(array.buffer_info())

# prints the number of occurrences of 3
print(array.count(3))

# prints the array in reverse order
array.reverse()
print(array)

# prints the array after removing 2 from it
array.remove(2)
print(array)

# prints the array after inserting 6 at 4th position
array.insert(3,6)
print(array)

# prints the array after popping 3rd element
array.pop(2)
print(array)

# prints the array after removing all elements
array.clear()
print(array)

# prints the array after extending it with [11,12,13]
array.extend([11,12,13])
print(array)

# prints the array after appending 20 at the end
array.append(20)
print(array)    

# prints the array after slicing it from index 1 to 4
print(array[1:4])   
