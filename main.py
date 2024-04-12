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

    #add in decode function
    
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
            #call decode function
            print("The encoded password is ", encoded_password, ", and the original password is ", decoded_password,".", sep="")
            print()
            continue
        elif option == 3:
            break

