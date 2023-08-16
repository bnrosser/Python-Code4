#
# Brandi Rosser
# May 23, 2023
# 
#
total = float(input("Enter the total purchase amount: $"))
member_status = input("Is the customer a loyalty program member (y/n): ")

if total <= 100 and member_status == 'y':
    discount = total * .15
    after = total - discount
    print(f"Total after discount: ${after:.2f}")

if total > 100 and member_status == 'y':
    discount2 = total * .25
    after = total - discount2
    print(f"Total after discount: ${after:.2f}")

if total > 100 and member_status == 'n':
    discount3 = total * .05
    after = total - discount3
    print(f"Total after discount: ${after:.2f}")

if total < 100 and member_status == 'n':
    discount4 = 0
    after = total - discount4
    print(f"No discount applied, total: ${after:.2f}")

sales_tax = after * .06
print(f"Sales tax: ${sales_tax:.2f}")

after_tax = after + sales_tax
print(f"Total after tax: ${after_tax:.2f}")
