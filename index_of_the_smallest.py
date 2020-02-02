def index_of_the_smallest(t): #voir verification sur la capture d'écran
  i=0
  j=1
  for elements in t:
      if t[i]<t[j]:
          return i
      else:
          return j