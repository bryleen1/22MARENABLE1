# file = open("file2.txt", "r")
# file.seek(0)
# print(file.readline())
# file.close

#file = open("file2.txt", "w")
# for n in range(1,11):
#      newline = "This is line" + str(n) + "\n"
#      file.write(newline)

# lines = file.readlines()
# print(lines)
# file.close

# file = open("filename.txt", "r")
# lines = file.readlines()
# print(lines)
# file.close

file = open("filename.txt", "r")

outfile = ""

for line in range(1, 10):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open("file2.txt", "w")
file.write(outfile)
file.close()

file = open("file2.txt", "r")
lines = file.readlines()
print(lines)
file.close