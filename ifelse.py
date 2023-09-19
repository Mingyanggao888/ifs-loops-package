age = int(input("Enter your age: "))

if age >= 21:
    print("Age greater or equal to 21.")
elif age >= 18:
    print("Age greater or equal to 18")
else:
    print("Too young.")

if age >= 18:
    if age >= 21:
    print("Age greater or equal to 21.")
    else:
    print("Age greater or equal to 18")
else:
    print("Too young.")