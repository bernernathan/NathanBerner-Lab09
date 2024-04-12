#Name: Nathan Berner
if __name__ == "__main__":
    def encode(password):
        encoded_password = ""
        for item in range(len(password)):
            if int(password[item]) == 9:
                encoded_password += 2
            elif int(password[item]) == 8:
                encoded_password += 1
            elif int(password[item]) == 7:
                encoded_password += 0
            else:
                encoded_password += str(int(password[item]) + 3)
        return encoded_password


    def decode(password):
        decoded_password = ""
        for item in range(len(password)):
            if int(password[item]) == 2:
                decoded_password += 9
            elif int(password[item]) == 1:
                decoded_password += 8
            elif int(password[item]) == 0:
                decoded_password += 7
            else:
                decoded_password += str(int(password[item]) - 3)
        return decoded_password
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))
        if option == 1:
            password = str(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
            print()
            encode(password)
            continue
        elif option == 2:
            encoded_password = encode(password)
            decoded_password = decode(encoded_password)
            print("The encoded password is ", encoded_password, ", and the original password is ", decoded_password,".", sep="")
            print()
            continue
        elif option == 3:
            break
