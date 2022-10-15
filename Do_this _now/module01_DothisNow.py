"""Module 01"""
# name = input("Name: ")
# print("Hello", name)

# get monthly_cost
# total_cost = monthly_cost * 12
# print total_cost

# monthly_cost = float(input("Monthly cost: "))
# total_cost = monthly_cost * 12
# print(f"The total is ${total_cost:.2f}")

# get gross pay, tax rate
# tax amount = gross pay * tax rate
# net pay = gross pay - tax amount
#  print net pay

# gross_pay = float(input("Gross pay: "))
# tax_rate = float(input("Tax rate: "))
# tax_amount = gross_pay * (tax_rate/100)
# net_pay = gross_pay - tax_amount
# print(f"Your net pay is ${net_pay:.2f}")

# age = int(input("Age: "))
# if age < 5:
#     category = "baby"
# elif age < 18:
#     category = "child"
# elif age < 66:
#     category = "adult"
# else:
#     category = "old"
# print(f"Your age {age} is considered {category}")
# SECRET = 4
# number = int(input("Guess a number between 1 and 10: "))
# while number != SECRET:
#     print("Guess again.")
#     number = int(input("Guess a number between 1 and 10: "))
# print("Correct!")

# age = int(input("Age: "))
# while age > 120 or age < 0:
#     print("Invalid age")
#     age = int(input("Age: "))
# if age < 5:
#     category = "baby"
# elif age < 18:
#     category = "child"
# elif age < 66:
#     category = "adult"
# else:
#     category = "old"
# print(f"Your age {age} is considered {category}")

# number = int(input("How many?: "))
# total = 0
# for i in range(number):
#     age = int(input("Age: "))
#     total = age + total
# print(f"Total: {total}")
# average = total / number
# print(f"Average: {average}")

total = 0
number = 0
age = int(input("Age: "))
while age > 0:
    total = age + total
    number = number + 1
    age = int(input("Age: "))
print(f"Total: {total}")
average = total / number
print(f"Average: {average}")


