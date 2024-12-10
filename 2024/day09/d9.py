def get_data():
    from os import path

    data = []
    spaces = []    

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            for i in range(0, len(line), 2):
                data.append(int(line[i]))
                
            for i in range(1, len(line), 2):
                spaces.append(int(line[i]))
    return data, spaces

class Storage:
    def __init__(self, data):
        self.data = {}
        
        for f, q in enumerate(data):
            self.data[f] = q
    
    def get_next(self):
        if len(list(self.data.keys())) > 0:
            f = min(list(self.data.keys()))
            q = self.data[f]
            self.data.pop(f)
            return [f] * q
        else:
            return None
        
    def get_tail(self):
        while len(list(self.data.keys())) > 0:
            f = max(list(self.data.keys()))
            q = self.data[f]
            self.data.pop(f)
            ans = [f] * q
            
            for i in ans:
                yield i
        return None

# This was my original part 1 which worked really nicely.  And then I discovered that it would have been a nightmare to do part 2 with the same logic.
def part1(data, spaces):
    answer = 0
    files = Storage(data)
    i = 0
    tail = files.get_tail()
    more_data = True
    more_spaces = True
    
    while more_data and more_spaces:
        cur_file = files.get_next()
        if cur_file is not None:
            for f in cur_file:
                answer += i * f
                i += 1
        else:
            more_data = False
        if spaces:
            s = spaces.pop(0)
            if s is not None:
                for a in range(s):
                    try:
                        f = next(tail)
                        answer += i * f
                        i += 1
                    except:
                        more_spaces = False
            else:
                more_spaces = False
    print('Part 1:  {}'.format(str(answer)))

def create_start(data, spaces):
    pattern = []
    i, j, f = 0, 0, 0
    
    while (i < len(data)) or (j < len(spaces)):
        if len(data) > 0:
            d = data.pop(0)
            pattern += ([f] * d)
            f += 1
        
        if len(spaces) > 0:
            s = spaces.pop(0)
            pattern += ([-1] * s)
            
    return pattern

def find_run(pattern, start):
    i = 0

    a = pattern[start]
    while (start + i <= (len(pattern) - 1)) and (pattern[start + i] == a):
        i += 1
        
    return i

def part1a(the_pattern):
    pattern = the_pattern[::]
    i = 0
    j = len(pattern) - 1
    
    while i < j:
        while pattern[i] != -1:
            i += 1
            
        while pattern[j] == -1:
            j -= 1

        if i < j:
            pattern[i], pattern[j]  = pattern[j], pattern[i]
        
    answer = 0
    i = 0
    
    while pattern[i] != -1:
        answer += pattern[i] * i
        i += 1
    print('Part 1:  {}'.format(str(answer)))

def find_opening(pattern, required_size):
    i = 0
    
    while i < len(pattern):
        while pattern[i] != -1:
            i += 1
            
        # We found a gap
        run = find_run(pattern, i)
        
        if run >= required_size:
            return i
        else:
            i += run
    return None
   
def part2(the_pattern):
    pattern = the_pattern[::]
    
    values = list(set(pattern))
    values.remove(-1)
    values.sort()
    
    while len(values) > 0:    
        value = values.pop()
        value_idx = pattern.index(value)
        data_run = find_run(pattern, value_idx)
        
        # Find an opening that will hold the data
        space_idx = find_opening(pattern, data_run)
        
        if space_idx is None:
            continue
        else:
            if space_idx < value_idx:
                for i in range(data_run):
                    pattern[value_idx + i], pattern[space_idx + i] = pattern[space_idx + i], pattern[value_idx + i]

    
    answer = 0
    i = 0
    
    while i < len(pattern):
        answer += max(pattern[i],0) * i
        i += 1
    print('Part 2:  {}'.format(str(answer)))


data, spaces = get_data()
pattern = create_start(data, spaces)
part1a(pattern)
part2(pattern)