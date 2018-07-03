numb = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and here is my flock", numb)

print("Now my biggest sheep has size", max(numb) ,"let's shear it")
index = numb.index(max(numb))
numb[index] = 8
print("After shering, hear  is my flock ", numb, sep = ", ")             