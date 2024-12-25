from collections import deque

def get_data():
    from os import path

    data = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            data.append(int(line.strip()))
    return data

def mix(secret, intermediate):
    return secret ^ intermediate

def prune(secret):
    return secret % 16777216

def generate_secrets(seed, keep_secrets = False):
    secret = seed
    secrets = []
    if keep_secrets:
        secrets.append(secret)
    for i in range(2000):
        a = secret *64
        secret = mix(secret, a)
        secret = prune(secret)
        b = secret // 32
        secret = mix(secret, b)
        secret = prune(secret)
        c = secret * 2048
        secret = mix(secret, c)
        secret = prune(secret)
        if keep_secrets:
            secrets.append(secret)
    if keep_secrets:
        return secrets
    else:
        return secret
        
def calculate_patterns(seed):
    patterns = {}
    que = deque([0], 4)
    last_price = 0
    
    secrets = generate_secrets(seed, True)
    for i, secret in enumerate(secrets):
        current_price = secret % 10
        que.append(current_price - last_price)
        if i >= 4:
            pattern = tuple(que)
            if pattern not in patterns.keys():
                patterns[pattern] = current_price
        last_price = current_price
    return patterns
        
def normalize_patterns(patterns):
    all_patterns = []
    for seed in patterns.keys():
        all_patterns += list(patterns[seed].keys())
    return set(all_patterns)
    
    

def part1(data):
    answer = 0
    for seed in data:
        answer += generate_secrets(seed)
        
    print('Part 1:  {}'.format(str(answer)))

def part2(data):
    answer = 0
    patterns = {}
    for seed in data:
        patterns[seed] = calculate_patterns(seed)
        
    all_patterns = normalize_patterns(patterns)
    for pattern in all_patterns:
        total = 0
        for seed in data:
            if pattern in patterns[seed].keys():
                total += patterns[seed][pattern]
        answer = max(answer, total)
        
    
    print('Part 2:  {}'.format(str(answer)))

data = get_data()
# part1(data)
part2(data)
