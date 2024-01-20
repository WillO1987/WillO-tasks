def fac(n):
    if n == 0:
        return 1 
    else:
        return n *fac(n-1)
    #endif
#endfunc

#print(fac(998))

number = [3, 6, 2, 8 , 1]
def calcAdd(n , number):
    if n == -1:
        return 0
    else:
        return number[n] + calcAdd(n-1, number)
    
print(calcAdd(len(number) -1 , number))


