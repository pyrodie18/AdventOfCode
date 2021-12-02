input = open("layers.txt", "r")
password = input.read()

layers=[]
length = 150
zeroCount = 200

for index in range (0, len(password), length):
	layers.append(password[index : index + length])
	
for layer in layers:
	count = 0
	for i in layer:
		if i == '0':
			count += 1
	if count < zeroCount:
		oneCount = 0
		twoCount = 0
		for n in layer:
			if n == '1':
				oneCount += 1
			elif n == '2':
				twoCount += 1
		answer = oneCount * twoCount
		print(answer)
		zeroCount = count
input.close()
