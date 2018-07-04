dict = {
    "hc": "học tập",
    "ng": "người",
    "pt": "phát triển",
    "eny": "Em người yêu",
    "any": "Anh người yêu",
    "ns": "Nói",
    "Ngta": "Người ta",
    "lm": "Làm",
    "r": "Rồi",
    "stt": "Status",
}
loop = True
while loop:
    for key in dict.keys():
        print(key, end="\t")
    print()
    code = input("Your code: ")
    if code in dict:
        print("Translation:",dict[code])
    else:
        print("Not Found")
        contribute = input("Do you want to contribute this word (Y/N)? ").lower()
        if contribute == "y":
            trans = input("Your translation: ")
            dict[code] = trans
        else:
            print("Bye")
            loop = False
    
