# Creating an Array 
# 1st menthod through Array module 

# import array
# my_arr = array.array("i", [1,2,3,4,5,6])
# print(my_arr)

# 2nd method through numpy
# import numpy as np

# np_arr = np.array([1,2,3,4])
# print(np_arr)

# Insertion in Array 

#At the begining 
# my_arr.insert(0, 19)
# print(my_arr)
# #IN the middle
# my_arr.insert(4, 109)
# print(my_arr)
#At the end
# my_arr.insert((len(my_arr)),190)


#Traversal in Array

# for i in range(len(my_arr)):
#     print(my_arr[i], end=" ")


#Acessing an element in Array

# def access_element(array, index):
#     if index >= len(array):
#         print("There is no value at this index.")
#     else:
#         print(array[index])

# access_element(my_arr, 2)

#Searching for an Element in the array
# def search(array, value):
#     for i in range(len(array)):
#         if array[i] == value:
#             print(f"value {value} is at index {i}.")
#     return -1

# search(my_arr, 101)

# Deleting an element in Array

# def delete(array, index):
#     n = len(array)
#     if index < 1 or index > n:
#         print("Invalid Position")
#     else:
#     # Shift elements to the left
#         for i in range(index - 1, n- 1):
#             array[i] = array[i + 1]

#     # Reduce the size by ignoring the last element
#     n= n-1

#     print("Array after deletion:")
#     for i in range(n):
#         print(array[i], end=" ")

     
# delete(my_arr, 9)

#---------------  Creating 2D array ----------------

import numpy as np

arr = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
print(arr)

#Insertion in 2D array
# new2Darray = np.insert(arr, 0, [[1,2,3,4]], axis=0) # axis 1 = column, axis 2 = row
# print(new2Darray)

#Acessing element in 2D Array
# def access_element(array, row, column):
#     if (row >= len(array)) or (column >= len(array[0])):
#         print("Incorrect Index")
#     else:
#         print(array[row][column])

#Traversal in 2D array
def show(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

# show(arr)

# Searching in 2D array
def search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                print(f"{value} is at index ({i},{j})")
    
    else:
        print("element not found.")

# search(arr, 9)

# Deleting 2D array

new_arr = np.delete(arr, 0, axis= 0) # 0 = row, 1 = column
print(new_arr)