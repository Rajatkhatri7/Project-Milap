# greedy algo big+small+more small+more moresmall


# A= x0<=x1<=x2.....x(n+1) = B

#n=B

# L is farthest reachable dist with full tank

def MinRefills(x,n,L):  
    numrefil=0,    # currently we r at starting node
    currentrefil=0

    while currentrefil<=n:
        lastrefill=currentrefil 

        while (currentrefil<=n and x[currentrefil+1]-x[lastrefill]<=L): # checking the farthest reachable gas s
            currentrefil+=1
        if currentrefil==lastrefill:
            return 0
        if currentrefil<=n:
            numrefil+=1

    return numrefil



"""
O(n) running time 

starting from 0 to n+1 for current refuils 
and 0 to n for numrefuils   






"""