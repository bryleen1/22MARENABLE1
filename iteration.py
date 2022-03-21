# Write a while loop which asks for the names of 5 people, 
# and for each person prints their name followed by the text "is awesome!"

counter= 1
"""
while counter <= 5:
    name = input("Enter your name ")
    print(f"{name} is awesome!")
    counter += 1
"""
#append into a list method then add is awesome from the list 
list1 = []
while counter <= 5:
    list1.append(input("Enter your name "))
    counter += 1

for name in list1:
    print(f"{name} is awesome!")