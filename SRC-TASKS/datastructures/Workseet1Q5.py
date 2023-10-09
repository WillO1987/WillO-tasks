S = "x"
p = "0"
num = 6
grid = [[S for i in range(6)] for p in range(6)]
gamerunning = True
while(gamerunning == True): 

    print("Enter a number on the grid, press x to exit") 

    # grid[x,y] = "x" 
    
    x = int(input())

    y = int(input())

    grid[x][y] = 0 
        
    #     for u in num:
    #         print(x, end = "")
    #     print()

    print(grid)

    if(x == "X" or y == "x"):  

        gamerunning == False 

    

 