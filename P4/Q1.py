# input for exam score
score = float(input("Enter a score : "))

#intialzize a grade as empty string
grade = ""

#Determine the grade based on the score from quetion table
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score < 90:
    grade = "B"
elif score >= 70 and score < 80:
    grade = "C"
elif score >= 60 and score < 70:
    grade = "D"
elif score >= 0 and score < 60:
    grade = "F"
else:
    grade = "Invalid score"

match grade:
    case "A"|"F":
        print("Your got an ", grade,  "for the test!")
    case "B"|"C"|"D":
        print("Your got a ", grade,  "for the test!")
    case _:
        print("You have enter a wrong input")
