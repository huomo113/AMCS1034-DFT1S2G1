hourly_rate =40.00
OT_regular= hourly_rate * 1.5
OT_excess= hourly_rate * 2
hourly_limit= 35
hourly_regular= 25


#read the hour input
hour = float(input("Enter working hour: "))

if hour <=35:
    regular_pay = hour * hourly_rate
else:
    regular_pay = hourly_limit * hourly_rate
    hour -= hourly_limit

if hour <= 25:
    OT_pay = hour * OT_regular
else:
    OT_pay = hourly_regular * OT_regular
    hour -= hourly_regular

OT_pay += hour * OT_excess

print("\n{:15s}: RM{:.2f}".format("Total salary", regular_pay + OT_pay))
print("\n{:15s}: RM{:.2f}".format("->Regular Pay", regular_pay))
print("\n{:15s}: RM{:.2f}".format("->Overtime Pay", OT_pay))
print("Total Salary :" + str(round(regular_pay + OT_pay ,2)))