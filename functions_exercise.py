"""
def add_calc(number1, number2):
    answer = number1 + number2
    return answer

added_number = add_calc(5,5)
print(added_number + 20)

print(add_calc(5,5) + 20) #tried to shorten the code
"""
#The program should take the students name, homework score (/25), assessment score (/50)
#and final exam score (/100) as inputs, and output their name and final ICT grade as a percentage.

""""
first attempt at answer, couldn't turn the parameters into inputs)

def assessment_calc(name, homework_score, assessment_score, final_exam_score):
    final_grade = (homework_score/25) + (assessment_score/50) + (final_exam_score/100) *100
    if final_grade > 85:
        return f"{name} your final grade is {final_grade} which is an A"
    elif final_grade > 65:
        return "{name} your final grade is {final_grade} which is a B"
    else:
        return f"{name} your final grade is {final_grade} which is a Fail"


print(assessment_calc("John", 25, 25, 60))
"""
#Earl's answer. Turn the parameters into variables
"""
def calc(hscore, ascore, escore):
    result = (hscore + ascore + escore) / 175 * 100    
    return round(result)

name = input("Enter the name: ")
hscore = int(input("Enter the Homework score: "))
ascore = int(input("Enter the Assessment score: "))
escore = int(input("Enter the Exam score: "))
result = calc(hscore, ascore, escore)

if result >= 80:
    grade = "A"
elif result >= 70:
    grade = "B"
elif result >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Student: {name}, Final grade: {grade}, with a percentage of: {result}%")

"""