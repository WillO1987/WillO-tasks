def calc(n):
    if n > 0:
        n = n + calc(n-1)
    #endif
    return n 
#endfunc

print(calc(5))