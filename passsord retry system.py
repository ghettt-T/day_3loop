attemps = 3
while attemps > 0:
    password = input("Enter Password: ")
    if password == "PASSWORD":
        print("Access granted")
        break
    else:
        attemps -= 1
        print("Attempts left: ", attemps)