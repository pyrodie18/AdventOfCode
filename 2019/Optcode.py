class OptCode():
    def __init__(self, code):
        self.instructions = []
        self.input_pos = 0
        for i in code.split(","):
            self.instructions.append(int(i))
            
    def get_value(self, position):
        return self.instructions[position]
    
    def set_value(self, position, value):
        self.instructions[position] = value
    
    def code1(self, pointer):
        p1 = self.parse_param(pointer, 1)
        p2 = self.parse_param(pointer, 2)
        output_loc = self.instructions[pointer + 3]
        self.instructions[output_loc] = p1 + p2
        
    def code2(self, pointer):
        p1 = self.parse_param(pointer, 1)
        p2 = self.parse_param(pointer, 2)
        output_loc = self.instructions[pointer + 3]
        self.instructions[output_loc] = p1 * p2
        
    def code3(self, pointer, values):
        output_loc = self.instructions[pointer + 1]
        self.instructions[output_loc] = values[self.input_pos]
        self.input_pos += 1
        
    def code4(self, pointer):
        output_val = self.parse_param(pointer, 1)
        print('Output:  Pointer: {}  Value:  {}'.format(str(pointer),str(output_val)))
        return self.instructions[pointer + 1]
    
    def code5(self, pointer):
        p1 = self.parse_param(pointer, 1)
        
        if p1 != 0:
            return self. parse_param(pointer, 2)
        else:
            return -1
        
    def code6(self, pointer):
        p1 = self.parse_param(pointer, 1)
        
        if p1 == 0:
            return self. parse_param(pointer, 2)
        else:
            return -1
        
    def code7(self, pointer):
        p1 = self.parse_param(pointer, 1)
        p2 = self.parse_param(pointer, 2)
        output_loc = self.instructions[pointer + 3]
        
        if p1 < p2:
            self.instructions[output_loc] = 1
        else:
            self.instructions[output_loc] = 0
            
    def code8(self, pointer):
        p1 = self.parse_param(pointer, 1)
        p2 = self.parse_param(pointer, 2)
        output_loc = self.instructions[pointer + 3]
        
        if p1 == p2:
            self.instructions[output_loc] = 1
        else:
            self.instructions[output_loc] = 0

    def get_opcode(self, instruction):
        return instruction % 100
    
    def parse_param(self, pointer, param):
        instruction = str(self.instructions[pointer])
        instruction = ("0" * (5-len(instruction)) + instruction)
        
        mode = int(instruction[-2 - param: -1 - param])
        
        # Immediate Mode
        if mode == 1:
            return self.instructions[pointer + param]
        else:
            return self.instructions[self.instructions[pointer + param]]  

    def run(self, INPUT_VALUES = None):
        OUTPUT_VALUE = None
        p = 0
        while p <= (len(self.instructions) - 1):
            opcode = self.get_opcode(self.instructions[p])
            match opcode:
                case 1:
                    self.code1(p)
                    p += 4
                case 2:
                    self.code2(p)
                    p += 4
                case 3:
                    self.code3(p, INPUT_VALUES)
                    p += 2
                case 4:
                    OUTPUT_VALUE = self.code4(p)
                    p += 2
                case 5:
                    pos = self.code5(p)
                    if pos >= 0:
                        p = pos
                    else:
                        p += 3
                case 6:
                    pos = self.code6(p)
                    if pos >= 0:
                        p = pos
                    else:
                        p += 3
                case 7:
                    self.code7(p)
                    p += 4
                case 8:
                    self.code8(p)
                    p += 4
                case 99:
                    if OUTPUT_VALUE is not None:
                        return self.instructions, OUTPUT_VALUE
                    else:
                        return self.instructions