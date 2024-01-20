import time
start_time = time.time()
time.sleep(3) #so that we can see how logng the code actually takes 

# def Fibonacci(n):
#     fibNumbers = [0,1]
#     for i in range(2,n+1):
#         fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
#     #next i
#     print(fibNumbers)
   

# Fibonacci(100)
# print ("--- %s seconds ---" % (time.time () - start_time))
# # print ("--- %s seconds ---" % (time.time () - start_time))

# def fibbonacci(n): 
#     if n== 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibbonacci(n-1) + fibbonacci(n-2)
# #endfunc
# fibbonacci(10)
# print ("--- %s seconds ---" % (time.time () - start_time))

calculations = [0, 1] #stores previously calculated solutions

def fibDyn(n):
    #base case: checks if solution has already been calculated
    if n < len(calculations):
        return calculations[n]
   
    currentSolution = fibDyn(n-2) + fibDyn(n-1)
    calculations.append(currentSolution)
    return currentSolution

print(fibDyn(6))

print(fibDyn(6))

print(fibDyn(5))
print(fibDyn(10))
print(fibDyn(9))
print(fibDyn(3  ))