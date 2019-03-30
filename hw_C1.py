a=[int(i) for i in input("Введите числа через пробел на этой строке: ").split()]
for i in range(1, len(a)):
	if a[i]>a[i-1]:
		print(a[i])
		
