#  for loops

power_rangers = ["Jason", "Trini", "Billy", "Zach", "Kim"]

for ranger in power_rangers:
    print(ranger)

power_rangers.append("Billy")
print(power_rangers)

power_rangers.remove("Billy")

print(power_rangers)

colors = ["red", "green", "blue"]

for idx, color in enumerate(colors):
    if color == "green":
        print(f"{idx}: {color}")
    else:
        print(f"{idx}: This is NOT green!")
