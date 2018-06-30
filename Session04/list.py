# print("Hi there, here your favorite things so far ")

list =["eating", "playing", "learning"]
# print(*list, sep=", ")
# new_list =input("Name one thing you want to add ")
# list.append(new_list)
# print(*list, sep=", ")
pos = int(input("Position you want to update? "))
update_list = input("Your replacing favotite? ")
list[pos - 1] = update_list
list.remove("learning")
print(" * "* 20)
for index, list in enumerate(list):
    print(index +1, list, sep=", ")
print(" * "* 20)