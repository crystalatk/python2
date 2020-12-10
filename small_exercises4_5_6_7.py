print("***4****")

numbers = [-2, -1, 0, 1, 2, 3, 4, 5, 6]

for every_number in numbers:
    if every_number % 2 == 0:
        print(every_number)


print("\n****5***")

for each_number in numbers:
    if each_number > 0:
        print(each_number)

print("\n***6***")
positive_numbers = []
for the_number in numbers:
    if the_number > 0:
        positive_numbers.append(the_number)

print(positive_numbers)

print("\n***7****")
product_list = []
factor = 5
for a_number in numbers:
    product = a_number * 5
    product_list.append(product)

print(product_list)
