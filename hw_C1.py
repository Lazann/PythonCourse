>>> a = (1,2,3,4,5,6,7,8,5,4,7,5,8,2)
>>> for i in range(1, len(a)):
	if a[i]>a[i-1]:
		print(a[i])
