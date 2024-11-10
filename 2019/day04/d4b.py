total = 0
for n in range (124075, 580769):
	num = [int(i) for i in str(n)]
	adjacent = 0
	decrease = 1
	
	#Check for adjacent values
	for i in range (0, 5):
		if num[i] == num[i+1]:
			if num.count(num[i]) == 2:
				adjacent = 1

	#Check for decrease
	for i in range (0, 5):
		if num[i+1] < num[i]:
			decrease = 0
			break
	
	if adjacent and decrease:
		total += 1
		print(n)
		
print(total)
