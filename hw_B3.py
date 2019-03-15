>>> s=list('GAGCCTACTAACGGGAT') 
>>> t=list('CATCGTAATGACGGCCT')	  
>>> HAMM = [(x,y) for x,y in zip(s,t) if x != y]	  
>>> print (len(HAMM))
