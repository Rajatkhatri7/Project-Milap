# greedy algo big+small+more small+more moresmall


# A= x0<=x1<=x2.....x(n+1) = B

#n=B


def minrefills(x,n,L):  
    numrefil=0,    # no refuils at starting
    currentrefil=0

    while currentrefil<=n:
        lastrefill=currentrefil 

        while (currentrefil<=n and x[currentrefil+1]-x[lastrefill]<=L):
            currentrefil+=1
        if currentrefil==lastrefill:
            return 0
        if currentrefil<=n:
            numrefil+=1

    return numrefil

