#Author: Emma Hsieh
#Date: 06/01/2022
#About: Given a choice to either encrypt or decrypt, the user will enter their message and desired key shift
#Preconditions: The given phrase must only include lowercase and uppercase letters - no special character or numbers; the shift must be an integer (can be negative OR positive)

#Functions
#Encrypting the Messsage
def cipherText(before_e, shift):
    #two lists for upper and lowercase letters.
    alphabet_lower = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    alphabet_upper = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    after_e = ""
    shift = shift % 26

    #checks if the first character is a space - else, shifts the character down the array for the new letter
    for x in before_e:
        if x.isspace() == False:
            if x.isupper() == True:
                #Uppercase Loop
                for e in range(len(alphabet_upper)):
                    if x == alphabet_upper[e]:
                        #used (26 - shift) to represent subtracting 26 then adding the shift, so it's within the array's range
                        if e >= (26 - shift):
                            #if the shift goes past z, it would be outside the array's range
                            after_e = after_e + alphabet_upper[e -
                                                               (26 - shift)]
                        else:
                            after_e = after_e + alphabet_upper[e + shift]
            else:
                #Lowercase Loop
                for e in range(len(alphabet_lower)):
                    if x == alphabet_lower[e]:
                        if e >= (26 - shift):
                            after_e = after_e + alphabet_lower[e -
                                                               (26 - shift)]
                        else:
                            after_e = after_e + alphabet_lower[e + shift]
        #if the character is a space, no change is needed
        else:
            after_e = after_e + x
    return after_e


#Second Function: Decrypting the Message
def plainText(before_d, shift):
    alphabet_lower = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    alphabet_upper = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    after_d = ""
    shift = shift % 26

    for x in before_d:
        if x.isspace() == False:
            if x.isupper() == True:
                #Uppercase Loop
                for d in range(len(alphabet_upper)):
                    if x == alphabet_upper[d]:
                        if d < shift:
                            #going backwards now, use the inverse of "(26 - shift)"
                            after_d = after_d + alphabet_upper[d +
                                                               (26 - shift)]
                        else:
                            #the inverse of "shift" is its opposite
                            after_d = after_d + alphabet_upper[d - shift]
            else:
                #Lowercase Loop
                for d in range(len(alphabet_lower)):
                    if x == alphabet_lower[d]:
                        if d < shift:
                            after_d = after_d + alphabet_lower[d +
                                                               (26 - shift)]
                        else:
                            after_d = after_d + alphabet_lower[d - shift]
        else:
            after_d = after_d + x
    return after_d


#Main Code:
#boolean variable to either continue or stop the while loop
cont = 1
while cont == 1:
    question = input(
        "Do you want to encrypt or decrypt a message? (encrypt/decrypt) ")
    if question == "encrypt":
        #asks user for the message they want encrypted
        before_en = input("Enter the message that you want encrypted here: ")
        shift = int(input("Enter the key shift: "))

        #new variable, so it doesn't override the previous ones
        encryption_string = cipherText(before_en, shift)
        print('''Your new encrypted message is "%s."''' % encryption_string)

    elif question == "decrypt":
        #asks user for the message they want decrypted
        before_de = input("Enter the message that you want decrypted here: ")
        shift = int(input("Enter the key shift: "))

        #new variable, so it doesn't override the previous ones
        decryption_string = plainText(before_de, shift)
        print('''Your new decrypted message is "%s."''' % decryption_string)
    else:
        print("Input Error.")

    #asks user to continue or not, using the boolean variable
    q = input("Do you want to encrypt/decrypt another message? (yes/no) ")
    if q == "no":
        print("Goodbye!")
        cont = 0
    elif q == "yes":
        print("")
        cont = 1
    else:
        print("Input Error.")
