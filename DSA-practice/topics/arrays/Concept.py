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

# This is how we can convert a list into an array
list1 = [1,2,3,4,5]
array1 = arr.array('i', list1)
print(array1)

# This is how we can convert a tuple into an array
tuple1 = (1,2,3,4,5)
array2 = arr.array('i', tuple1)
print(array2)

# This is how we can convert a string into an array
string1 = "hello"
array3 = arr.array('u', string1)
print(array3)

# This is how we can convert a set into an array
set1 = {1,2,3,4,5}
array4 = arr.array('i', set1)
print(array4)

# This is how we can convert a dictionary into an array
dict1 = {1:'a', 2:'b', 3:'c'}
array5 = arr.array('i', dict1.keys())
print(array5)
array6 = arr.array('u', dict1.values())
print(array6)

# This is how we can convert a range into an array
range1 = range(1,6)
array7 = arr.array('i', range1)
print(array7)

# This is how we take input from the user to create an array
n = int(input("Enter the number of elements in the array: "))
array8 = arr.array('i', [])
for i in range(n):
    element = int(input("Enter element: "))
    array8.append(element)
print(array8)
