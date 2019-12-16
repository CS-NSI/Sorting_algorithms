def index_of_the_smallest(t):
    i=0
    j=1
    for element in t:
        if t[i]<t[j]:
            return i
        else:
            return j
