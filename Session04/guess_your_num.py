print("Guess your number name")
print("Now think of a number (0 - 100), then press Enter")
input()

print("""
All you have to do is to answer to my guess
'c' if my number is 'C'orrect
's' if my number is 'S'maller than your number
'l' if my number is 'L'arger than your number
""")

low = 0
high = 100
playing = True

while playing:
    mid = (low + high) // 2
    ans = input("Is {0} your number:".format(mid)).upper()

    if ans == "C":
        print("I knew it!!")
        playing = False
    elif ans == "S":
        low = mid
    elif ans == "L":
        high = mid
    else:
        playing = False
    





