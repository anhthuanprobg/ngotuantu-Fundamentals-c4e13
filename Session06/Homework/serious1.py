numb = int(input("Enter a number: "))
m = 0

for i in range (1, numb):
    if numb % i == 0:
        m += i
if m == numb:
    print("{0} is a perfect number".format(numb))
else:
    print("{0} is a not perfect number".format(numb))