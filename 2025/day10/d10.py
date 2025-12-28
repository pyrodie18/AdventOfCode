from itertools import combinations
from collections import defaultdict

def get_data():
    from os import path

    data = []
    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            a = {}
            line = line.strip().split()
            
            # Convert diagram into bitmask
            diagram = line[0][1:-1]
            diagram = diagram.replace(".", "0")
            diagram = diagram.replace("#", "1")
            a["diagram"] = int(diagram, 2)
            
            buttons = defaultdict(dict)
            for c, seq in enumerate(line[1:-1]):
                c = chr(65 + c)
                # build button bitmask
                bitmask_tmp = ["0"] * len(diagram)
                raw_tmp = []
                seq = seq[1:-1]
                seq = seq.split(",")
                for i in seq:
                    bitmask_tmp[int(i)] = "1"
                    raw_tmp.append(int(i))
                buttons[c]["bitmask"] = int("".join(bitmask_tmp),2)
                buttons[c]["raw"] = tuple(raw_tmp)
            a["buttons"] = buttons
            
            joltage = line[-1][1:-1]
            joltage = joltage.split(",")
            for i, j in enumerate(joltage):
                joltage[i] = int(j)
            a["joltage"] = joltage
            
            data.append(a)
                
    return data

def find_sequence(current_data):
    buttons = current_data["buttons"]
    
    for i in range(1, len(buttons)):
        C = combinations(buttons.keys(),i)
        for c in C:
            int_xor = current_data["diagram"]
            for b in c:
                int_xor = int_xor ^ buttons[b]["bitmask"]
            if int_xor == 0:
                return len(list(c))

def build_joltage_mapping(schematic):
    from collections import defaultdict
    J = defaultdict(dict)
    for i, j in enumerate(schematic["joltage"]):
        J[i]["joltage"] = j
        J[i]["buttons"] = []

    for b in schematic["buttons"].keys():
        for r in schematic["buttons"][b]["raw"]:
            J[r]["buttons"].append(b)
    return J

def solve(s):
    import pulp
    
    buttons = []
    for r in s.keys():
        buttons += s[r]["buttons"]
    buttons = tuple(set(buttons))
    
    P = pulp.LpProblem("register_buttons")
    
    # Create Vars
    V = {B: pulp.LpVariable(f"{B}_Button_Push", lowBound=0, cat="Integer") for B in buttons}
    
    # Create Objective
    P += pulp.lpSum(V.values()), "Button_Pushes"
    
    # Create Constraints
    for r in s.keys():
        joltage = s[r]["joltage"]
        buttons = s[r]["buttons"]
        exp = [1 * V[B] for B in buttons]
        P += (pulp.lpSum(exp) == joltage), f"reg_{r}_target"
    
    status = P.solve(pulp.PULP_CBC_CMD(msg=False))
    return int(pulp.value(P.objective))

def part1(data):
    answer = 0
    for s in data:
        answer += find_sequence(s)
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    for s in data:
        s = build_joltage_mapping(s)
        answer += solve(s)
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
part1(data)
part2(data)