>>> X=str.maketrans("ATGC", "TACG")	  
>>> s='AAAACCCGGT'	  
>>> sc=(s.translate(X)[::-1])	  
>>> print (sc)
