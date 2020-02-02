def insertion_sort_in_place(t): #voir verification sur la capture d'écran
    for i in range(1,len(t)):
        insert(t,i)

def insert(t,i):
    for current_index in range(i-1,-1,-1):
        if t[current_index] > t[current_index+1]:
            swap(t,current_index,current_index+1)
        else:
            break