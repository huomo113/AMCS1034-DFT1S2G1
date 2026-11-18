num_studennt = int(input("Enter the number of students: "))

Highest = 0
Second_score = 0
total = 0

for i in range(1, num_studennt + 1):
    if i % 100 == 11 or i % 100 == 12 or i % 100 == 13:
        suffix = "th"
    else:
        match i % 10:
            case 1:
                suffix = "st"
            case 2:
                suffix = "nd"
            case 3:
                suffix = "rd"
            case _:
                suffix = "th"

    score = float(input(f"Enter the {i}{suffix} student : "))

    if score > Highest:
        Second_score = Highest
        Highest = score
    elif score > Second_score and score < Highest:
        Second_score = score

    total += score

average = total / num_studennt

print(f"Highest : {Highest:.2f}%")
print(f"Second highest score: {Second_score:.2f}%")
print(f"Average score: {average:.2f}%")