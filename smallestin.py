def smallestin(t,i,j): #voir verification sur la capture d'écran
    res=t[i]
    for indice in range(i+1,j+1):
        if t[indice]<res:
            res=t[indice]
    return res
