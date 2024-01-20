
alist = [1, 3, 4, 6, 8, 9]
blist = [2,5,12,14,17]
clist = [0 for _ in range(len(alist)+len(blist))]


def merge(clist, alist, blist):
    pointera = 0 
    pointerb  = 0 
    pointerc = 0
    while pointera <= len(alist):
       
        if alist[pointera] < blist[pointerb]:
            clist[pointerc] = alist[pointera]
            pointera +=1
            pointerc +=1
        else:
            clist[pointerc] = blist[pointerb]
            pointerb +=1
            pointerc +=1
    #endwhile
    while pointerb >= len(blist):
        if pointera > len(alist):
            clist[pointerb] = blist[pointerb]
            pointerb +=1
            pointerc +=1
        
    #endwhile
merge(clist, alist, blist)