
# cypher = []
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
input = input("Enter a password") # user enters password and is stored
# for i in range (len(input)):#loops round for each char in string
#     cypher.append(input[i]) # puts each char in its own position in array
# #endfor
# shift = 3
# #for i in cypher[i]:
# for char in cypher[i]:
#     if char.isalpha():
#         char_shift = chr((ord('a') + shift % 26) + ord('a'))
#         cypher += char_shift
# print(cypher)

# The Encryption Function
print()
def cipher_encrypt(input, shift):

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

        elif c.isdigit():

            # if it's a number,shift its actual value 
            i_new = (int(i) + key) % 10

            encrypted += str(i_new)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += i

    return encrypted