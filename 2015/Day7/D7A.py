FileInput = open(".\Day7\D7_Input.txt", "r")
Instructions = FileInput.readlines()
Outputs = []

Counter = 0
for Instruction in Instructions:
    Step = Instruction.split()
    Instructions[Counter] = Step
    Counter += 1
    Outputs.append([Step[-1],''])

def AddOutput(value, Wire, Outputs):
    for i in range(len(Outputs)):
        if Outputs[i][0] == Wire:
            Outputs[i][1] = int(value)
            break
    return Outputs
    

def GetValue (Wire, Output):
    for Output in Outputs:
        if Output[0] == Wire:
            if Output[1] != '':
                return Output[1]
            else:
                return -1
            break


def BitAND (Instruction, Output):
    if Instruction[0].isdigit():
        Input1 = int(Instruction[0])
    else:
        Input1 = GetValue(Instruction[0], Output)
    Input2 = GetValue(Instruction[2], Output)
    if Input1 < 0 or Input2 < 0:
        return -1
    else:
        return Input1 & Input2


def BitOR (Instruction, Output):
    Input1 = GetValue(Instruction[0], Output)
    Input2 = GetValue(Instruction[2], Output)
    if Input1 < 0 or Input2 < 0:
        return -1
    else:
        return Input1 | Input2

def BitNOT (Instruction, Output):
    Input1 = GetValue(Instruction[1], Output)
    if Input1 < 0:
        return -1
    else:
        return ~ Input1 & 0xffff

def RShift (Instruction, Output):
    Input1 = GetValue(Instruction[0], Output)
    NumBytes = int(Instruction[2])
    if Input1 < 0:
        return -1
    else:
        return Input1 >> NumBytes

def LShift (Instruction, Output):
    Input1 = GetValue(Instruction[0], Output)
    NumBytes = int(Instruction[2])
    if Input1 < 0:
        return -1
    else:
        return Input1 << NumBytes

counter = 1
while True:
    MissingValue = 0
    for Instruction in Instructions:
        if GetValue(Instruction[-1], Outputs) == -1:
            if "AND" in Instruction:
                value = BitAND(Instruction, Outputs)
            elif "OR" in Instruction:
                value = BitOR(Instruction, Outputs)
            elif "NOT" in Instruction:
                value = BitNOT(Instruction, Outputs)
            elif "RSHIFT" in Instruction:
                value = RShift(Instruction, Outputs)
            elif "LSHIFT" in Instruction:
                value = LShift(Instruction, Outputs)
            else:
                if Instruction[0].isdigit():
                    value = int(Instruction[0])
                else:
                    value = GetValue(Instruction[0], Outputs)
            
            if value != -1:
                if Instruction[-1] == 'a':
                    print("Stop")
                Outputs = AddOutput(value, Instruction[-1], Outputs)
            else:
                MissingValue = 1
    if MissingValue == 0:
        break
    if counter > 1000:
        print("ran out")
        break
    counter += 1
print(Outputs)