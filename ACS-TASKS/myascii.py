for i in range(65, 91):
    print(ascii(i))
    print(chr(i))
    print(chr(i^ 0b00100000)) # makesit lowercase 