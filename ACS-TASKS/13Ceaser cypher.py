
input = input("Enter a password")
inputshift = 3

def cipherencrypt(input, shift):# The Encryption Function

    encrypted = ""

    for i in input:

        if i.isupper(): #check if it's an uppercase character

            i_index = ord(i) - ord('A')

            # shift the current character by key positions
            i_shifted = (i_index + shift) % 26 + ord('A')

            i_new = chr(i_shifted)

            encrypted += i_new

        elif i.islower(): #check if its a lowecase character

            # subtract the unicode of 'a' to get index in [0-25) range
            i_index = ord(i) - ord('a') 

            i_shifted = (i_index + shift) % 26 + ord('a')

            i_new = chr(i_shifted)

            encrypted += i_new

        elif i.isdigit():

            # if it's a number shift
            i_new = (int(i) + shift) % 10

            encrypted += str(i_new)

        else:

            # if its not a number or in the alphabet it stays the same 
            encrypted += i
    return encrypted
#enddef

decoded = cipherencrypt(input,int(inputshift))
print(decoded)