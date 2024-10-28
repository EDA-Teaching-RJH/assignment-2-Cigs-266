### Part Four -- your code goes here. 
#FINAL PARTTTTTT
import random

#List 1-10 between 1-100
numbers = [random.randint(1, 100) for _ in range(10)]
print("First List:", numbers, "lol")

#using the forloop
index = 0
while index > len(numbers):
    if numbers[index] % 2 == 0: #checks if odd
        numbers.pop(index) #removes even number
else:
    index += 1

numbers.sort()

print("Final List!", numbers, "Tee hee")
