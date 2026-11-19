#set interest rate
annual_interest = 0.05
monthly_interest = annual_interest / 12

#set amount to be save monthly
base = 100
total = 0
repetitions = 10
month = ""

print("{:10s}{:10s}".format("Month", "Total"))
for count in range(repetitions):
    total = (base + total) * (1 + monthly_interest)

    match (count + 1)%10:
        case 1:
            month = str(count + 1) + "st"
        case 2:
            month = str(count + 1) + "nd"
        case 3:
            month = str(count + 1) + "rd"  
        case _:
            month = str(count + 1) + "th"

    print("{:10s}RM {:<10.2f}".format(month, total))