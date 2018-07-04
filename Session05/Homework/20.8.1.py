let_input=input("This is a string with Uper and lower case Letters  ").lower()
letter = {
    "a": 2,
    "c": 1,
    "d": 1,
    "e": 5,
    "g": 1,
    "h": 2,
    "i": 4,
    "l": 2,
    "n": 2,
    "o": 1,
    "p": 2,
    "r": 4,
    "s": 5,
    "t": 5,
    "u": 1,
    "w": 2
}
count={}
for char in let_input:
    if char in letter:
        
        if char in count:
            count[char]=count[char]+1
        
        else:
            count[char]=1

countkeys=sorted(count)
for key in countkeys:
    print(key,count[key])
            