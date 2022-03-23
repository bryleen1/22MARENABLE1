# file1 = open("filename.txt", "r")
# print(file1.read())
# file1.close

# with open("filename.txt") as file2:
#     print(file2.readline())

# file1 = open("filename.txt", "r")
# print(file1.readlines())
# file1.close

# with open("filename.txt") as file3:
#     for num in file3:
#         print(num)

# with open("text.txt","w") as file:
#     file.write("I am learning Python!\n")
#     file.write("I am really enjoying it!\n")
#     file.write("And I want to add more lines to say how much I like it")

# with open("text.txt","a") as file:
#     file.write("What I want to add on goes here")

# with open("text.txt","a") as file:
#     file.write("\nWhat I want to add on goes here")

# with open("text.txt","a") as file:
#     file.write("\nI am adding in more lines\n")
#     file.write("And more…")

with open("text.txt") as file:
    print(file.read())

