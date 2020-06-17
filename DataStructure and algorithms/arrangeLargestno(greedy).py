# greedy algo big+small+more small+more moresmall

def minrefills(x,n,L):
    numrefil=0,
    currentrefil=0
    while currentrefil<n:
        lastrefill=currentrefil
        while currentrefil<n and x[currentrefil+1]-x[lastrefill]<L:
            currentrefil+=1
        if currentrefil==lastrefill:
            return 0
        if currentrefil<n:
            numrefil+=1

    return numrefil

