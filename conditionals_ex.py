# age = int(input("Enter your age: "))

# if age >= 85:
#     print("You are above 85")
# elif age >= 50:
#     print("You are between 50 and 85")
# elif age >= 20:
#     print("You are between 20 and 50")
# else:
#     print("You are below 20 years old")
'''
Asks for an input from the user as a mark.
If the mark is greater that 85 print "Distinction"
If the mark is between 65 and 85 print "Pass"
Anything else print "Fail"
'''

mark = int(input("Enter your mark "))
if mark > 85:
    print("Distinction")
elif mark >=65:
    print("Pass")
else:
    print("Fail")