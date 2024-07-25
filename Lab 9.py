def encode(password):
    newPassword = []
    for char in password:
        newChar = (int(char) + 3) % 10
        newPassword.append(str(newChar))
    return "".join(newPassword)


# decode code
def decode(password):
    newPassword = ""
    for i in range(len(password)):
        newPassword += str(int(password[i]) - 3)
    return newPassword

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = int(input(("Please enter an option: ")))

        if option == 1:
            password = input("Please enter the password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        elif option == 3:
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
