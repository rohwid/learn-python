def printinfo(arg1, *vartuple):
	print("Output is: ")
	print(arg1)
	for var in vartuple:
		print(var)
	return

printinfo(10)
printinfo(20, 30)
printinfo(40, 50, 60)
printinfo(70, 80, 90, 100)
