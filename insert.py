def insert(t,i): #ok
    for current_index in range(i-1,-1,-1):
        if t[current_index] > t[current_index+1]:
            swap(t,current_index,current_index+1)
        else:
            break