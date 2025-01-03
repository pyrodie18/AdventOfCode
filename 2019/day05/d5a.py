from os import path

# Variables
TestID = 1
CurrentPointer = 0 #Current instruction pointer
Incriment = 0


# Function Definitions
def get_opcode(Instruction):
    Opcode = Instruction % 100
    return Opcode

def get_parameter(Instruction, Code, ParamNum, CurrentPointer):
    Instruction = str(Instruction)
    Instruction = ("0" * (5-len(Instruction)) + Instruction)

    # Extract the Paramater Mode
    if (ParamNum == 1):
        Mode = int(Instruction[-3:-2])
    elif (ParamNum == 2):
        Mode = int(Instruction[-4:-3])
    elif (ParamNum == 3):
        Value = Code[CurrentPointer + ParamNum]
        return Value

    if (Mode == 0): # Postition
        Pos = Code[CurrentPointer + ParamNum]
        Value = Code[Pos]
    elif (Mode == 1): # Immediate
        Value = Code[CurrentPointer + ParamNum]
    return Value

input = open(path.join(path.dirname(__file__), 'input.txt'), 'r')
OriginalCode = input.read()
OriginalCode = OriginalCode.split(",")

# Load the instructions into memory
TotalInstructionCount = len(OriginalCode)

for i in range(TotalInstructionCount):
    OriginalCode[i] = int(OriginalCode[i])

Code = OriginalCode

while CurrentPointer <= TotalInstructionCount:
    print("In Loop.  Current Pointer {}", CurrentPointer)
    Instruction = Code[CurrentPointer]
    OpCode = get_opcode(Instruction)
    
    if (OpCode == 1):  # Addition
        Incriment = 4
        a = get_parameter(Instruction, Code, 1, CurrentPointer)
        b = get_parameter(Instruction, Code, 2, CurrentPointer)
        OutputLoc = get_parameter(Instruction, Code, 3, CurrentPointer)
        Answer = a + b
        Code[OutputLoc] = Answer

    elif (OpCode == 2):  # Multiplication
        Incriment = 4
        a = get_parameter(Instruction, Code, 1, CurrentPointer)
        b = get_parameter(Instruction, Code, 2, CurrentPointer)
        OutputLoc = get_parameter(Instruction, Code, 3, CurrentPointer)
        Answer = a * b
        Code[OutputLoc] = Answer

    elif (OpCode == 3):  # Input
        Incriment = 2
        OutputLoc = get_parameter(Instruction, Code, 1, CurrentPointer)
        Code[OutputLoc] = TestID

    elif (OpCode == 4):  # Output Location
        Incriment = 2
        a = get_parameter(Instruction, Code, 1, CurrentPointer)
        print(a)
    elif (OpCode == 99):  # Exit
        break

    CurrentPointer += Incriment 
print(Code)
