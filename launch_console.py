print("Welcome to Avek's launch console!")

while True:
    print("1) About me")
    print("2) My goals")
    print("3) Quit")
    match input(">> "):
        case "1": print("14-year-old aspiring coder, proficient in JavaScript, C++, and HTML.")
        case "2": print("I aspire to go to college in 2027, and dual major in Computer Science and Physics.")
        case "3": break
        case _: print("Please pick 1, 2, or 3.")