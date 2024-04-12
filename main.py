#Name: Nathan Berner
if __name__ == "__main__":
    def encode(password):
        encoded_password = ""
        for item in range(len(password)):
            if int(password[item]) == 9:
                encoded_password += '2'
            elif int(password[item]) == 8:
                encoded_password += '1'
            elif int(password[item]) == 7:
                encoded_password += '0'
            else:
                encoded_password += str(int(password[item]) + 3)
        return encoded_password

    #add in decode function
    def decode(encoded_pass):
        temp_pass_list = [int(val) for val in encoded_pass]
        for i in range(len(temp_pass_list)):
            if temp_pass_list[i] - 3 >= 0:
                temp_pass_list[i] -= 3
            else:
                temp_pass_list[i] = (temp_pass_list[i] - 3) + 10

        dec_pass_list = [str(val) for val in temp_pass_list]
        dec_pass = ''.join(dec_pass_list)
        return dec_pass


    enc_pass = 0
    dec_pass = 0
    
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
            enc_pass = encode(password)
            continue
        elif option == 2:
            dec_pass = decode(enc_pass)
            print("The encoded password is ", enc_pass, ", and the original password is ", dec_pass,".", sep="")
            print()
            continue
        elif option == 3:
            break

