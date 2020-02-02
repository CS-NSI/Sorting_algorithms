def my_sort(t): #voir verification sur la capture d'écran
    for j in range(1, len(t)):
        T = t[j]
        i = j - 1
        while i>= 0 and t [i] > T:
            t[i+1] = t[i]
            i = i-1
        t[i+1] = T
    return t

