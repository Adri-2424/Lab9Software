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
