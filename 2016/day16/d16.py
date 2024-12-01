INIT = "00111101111101000"
LENGTH = 272

def generate_curve(value):
    reverse = value[::-1]
    reverse = reverse.replace('0', '2')
    reverse = reverse.replace('1', '0')
    reverse = reverse.replace('2', '1')
    return value + '0' + reverse

def generate_checksum(value):
    checksum = ""
    for i in range(0, len(value) - 1, 2 ):
        if value[i] == value[i + 1]:
            checksum += "1"
        else:
            checksum += "0"
            
    if len(checksum) % 2 == 0:
        checksum = generate_checksum(checksum)
        
    return checksum
        

def part1():
    value = INIT
    while len(value) < 272:
        value = generate_curve(value)
        
    # Trim value
    value = value[:272]
    
    checksum = generate_checksum(value)
    print('Part 1:  {}'.format(str(checksum)))

def part2():
    value = INIT
    while len(value) < 35651584:
        value = generate_curve(value)
        
    # Trim value
    value = value[:35651584]
    
    checksum = generate_checksum(value)
    print('Part 2:  {}'.format(str(checksum)))

part1()
part2()