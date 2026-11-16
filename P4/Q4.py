value = int(input("Enter sales value (RM):"))

if value >=10001 and value <= 100000:
    sales1th = 1000
    sales2th = 8999
    sales3th = value - sales1th - sales2th
    commission = (sales3th * 0.10) + (sales2th * 0.05) + (sales1th * 0.01)
elif value >= 1001 and value <= 10000:
    sales1th = 1000
    sales2th = value - sales1th
    commission = (sales2th * 0.05) + (sales1th * 0.01)
elif value >= 0 and value <= 1000:
    commission = value * 0.01

print(f"Commission: RM {commission:.2f}")