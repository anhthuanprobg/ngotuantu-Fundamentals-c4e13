numbers = [-1, 20, 0, -10, 5, -100, 2018]
sorted_list = []
sorting = True
while len(numbers) > 0:
    min_numb = min(numbers)
    sorted_list.append(min_numb)
    numbers.remove(min_numb)


    if len(numbers) == 0:
        sorting = False

print(*sorted_list)

    