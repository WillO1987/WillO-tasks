Outlet1Sales = [10, 12, 15, 10]
Outlet2Sales = [5, 8 , 3, 6]
Outlet3Sales = [10, 12, 15, 10]

MAX = 4


for qtr in range(MAX): 
    total = Outlet1Sales[qtr] + Outlet2Sales[qtr] + Outlet3Sales[qtr]
    print("total for quarter, ", qtr + 1, total)
#next wtr