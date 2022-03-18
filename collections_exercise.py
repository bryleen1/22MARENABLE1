newbooks = {'Margaret Atwood': ["The Handmaiden's Tale", "A men"], 'J.R.R. Tolkien': 'The Hobbit', 'Roald Dahl': 'Charlie and the Chocolate Factory'}
start = input("Enter author name ")
#print(newbooks[start])
#print(f"{start} : {newbooks[start]}")
str1 = ", ".join(sorted(newbooks[start])) #string (join), alphabetical order (sorted)
print(str1)