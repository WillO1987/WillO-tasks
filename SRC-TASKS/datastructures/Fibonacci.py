import time
start_time = time.time()
time.sleep(3) #so that we can see how logng the code actually takes 
def Fibonacci(n):
    fibNumbers = [0,1]
    for i in range(2,n+1):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    #next i
    print(fibNumbers)
   

Fibonacci(10)

print ("--- %s seconds ---" % (time.time () - start_time))

# def fibbonacci(n): 
#     if n== 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibbonacci(n-1) + fibbonacci(n-2)
# #endfunc
# fibbonacci(2)
# print ("--- %s seconds ---" % (time.time () - start_time))