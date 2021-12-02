input = open("layers.txt", "r")
password = input.read()

layers = []
answer = []
length = 150
zeroCount = 200

for index in range (0, len(password), length):
	layers.append(password[index : index + length])

#Break it up into individual cells	
for layer in layers:
	layer = list(layer)
	
for c in range (0, 150):
	for layer in layers:
		if int(layer[c]) < 2:
			answer.append(layer[c])
			break

print(answer)
