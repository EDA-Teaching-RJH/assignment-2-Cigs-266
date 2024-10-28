### Part Three -- your code goes here. 
#First list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

#sorting
numbers.sort()

#removing "1"
numbers = [num for num in numbers if num != 1]

#extend list with 7, 8
numbers.extend ([7, 8])

print("Final List!", numbers)