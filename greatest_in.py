def greatest_in(t): #voir verification sur la capture d'écran
    res = t[0]
    for element in t:
        if element>res:
            res = element
    return res
