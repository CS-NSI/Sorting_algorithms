def greatest_in(t):
    res = t[0]
    for element in t:
        if element>res:
            res = element
    return res