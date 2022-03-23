"""
Create a new Python file which does the following:

Edits your "teams.txt" file so that the top line is replaced with "This is a new line".
Print out the edited file line by line.

"""
# with open("teams.txt", "w") as file:
#      file.write("This is a new line\n")
#      file.write("Team 2\n")
#      file.write("Team 3\n")
#      file.write("Team 4\n")
#      file.write("Team 5\n")

with open("teams.txt") as file:
    print(file.read())