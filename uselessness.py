one = "1"
zero = "0"

one_hundred = int(one+zero+zero)

useless = 0

while(useless < one_hundred):
	print("Useless "+str(useless+1))
	useless = useless + 1
	
if 100 == useless:
	print("Uselessness unconfirmed")
else:
	print("Uselessness confirmed")
