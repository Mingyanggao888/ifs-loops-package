name = input("Enter your name: ")
age = int(input("Enter your age: "))
national = input("Since you are too young, we must ask for your nationality [US/EU]: ")

# print("Hello {}!".format(name, age))
print(f"Hello {name}! Age: {age}")

print('-‘ * 50)

# Check if the user is older than 21 years of age

enter_club_bool = (age >= 21)

if enter_club_bool:
    print("Checking your age...")
    print("This may take a while...")
    print(f"Welcome {name}! You can enter the club!")
elif age >= 18 and national == "EU":
    print(f"Welcome {name}! You are from the EU and you can enter the club!")
elif name == "Martin":
    print(f"Welcome {name} you can enter the club!")
else:
    print(f"I'm sorry {name}, you are from the US and you cannot enter the club. You are too young.")

#if age < 21:
#  print("Making sure you are 20 or younger...")
#  national = input("Since you are too young, we must ask for your nationality [US/EU]: ")
#   if national == "EU" and age >= 18:
#     print(f"Welcome {name}! You are from the EU and you can enter the club!")
#else:
#       print(f"I'm sorry {name}, you are from the US and you cannot enter the club. You are too young.")

print('-‘ * 50)

print("All the actions are done!")