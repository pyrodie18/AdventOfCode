input = open("intcode.txt", "r")
code = input.read()
code = code.split(",")
 
for i in range(len(code)):
    code[i] = int(code[i])
 
print(code)
 
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
 
print(code)
