
print("""Welcome user! 
Please note that you will need to enter the number and the weight of each item you want to send. 
The allowed range of each item is from 1 kg to 10 kg and the limit per package is 20kg. """)

MAX_PACKAGE_WEIGHT = 20
ITEM_WEIGHT_MIN = 1
ITEM_WEIGHT_MAX = 10

items_to_be_shipped = int(input("Enter the number of items to be shipped:"))

package_weight = 0
weight_sent = 0
number_of_packages_sent = 0
index_most_empty_package = 0
lightest_package = 20

correct_items = 0
while correct_items < items_to_be_shipped:
    item_weight = int(input("Enter the weight of the next item: "))
    if item_weight == 0:
        print("Ending the packaging.")
        break
    elif item_weight < 1 or item_weight > 10:
        print("You must enter weights between 1 and 10")
        continue
    else:
        correct_items += 1
        package_weight += item_weight

        if package_weight > 20:
            package_weight -= item_weight
            number_of_packages_sent += 1
            weight_sent += package_weight

            if package_weight < lightest_package:
                lightest_package = package_weight
                index_most_empty_package = number_of_packages_sent
            package_weight = item_weight


if package_weight > 0:
    number_of_packages_sent += 1
    weight_sent += package_weight

    if package_weight < lightest_package:
       lightest_package = package_weight
       index_most_empty_package = number_of_packages_sent

unused_capacity = number_of_packages_sent * 20 - weight_sent

print(f"Number of packages sent: {number_of_packages_sent}")
print(f"Total weight of packages: {weight_sent}")
print(f"Total unused capacity: {unused_capacity}")
print(f"Package number with the most unused kilograms: {index_most_empty_package}")