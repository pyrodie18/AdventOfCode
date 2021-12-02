input = open("intcode.txt", "r")
originalcode = input.read()
originalcode = originalcode.split(",")
 
for i in range(len(originalcode)):
	originalcode[i] = int(originalcode[i])

 
for noun in range (1, 100):
#	print("noun " + str(noun))
	for verb in range (1, 100):
		code = [x for x in originalcode]
#		print("verb " + str(verb))
		code[1] = noun
		code[2] = verb
		for i in range(0, len(code)-1, 4):
			opcode = code[i]
			i1 = code[i+1]
			i2 = code[i+2]
			i3 = code[i+3]
			if (opcode == 1):
				code[i3] = code[i1] + code[i2]
			elif (opcode == 2):
				code[i3] = code[i1] * code[i2]
			elif (opcode == 99):
				break
		if (code[0] == 19690720):
			print (noun, verb)
