print("1. Multiplication")
print("2. Subtraction")
print("3. Division")
print("4. Addition")

choice = input("enter your choice: ")

a = float(input("enter first number: "))
b = float(input("enter second number: "))

if choice == "1":
    print(a * b)
elif choice == "2":
    print(a - b)
elif choice == "3":
    print(a / b)
else:
    print(a + b)
