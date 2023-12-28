def get_input():
    from os import path

    input = []

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            input.append(line.strip())
    return input


def find_hypernets(network):
    import re

    a = re.findall(r"\[(\w+)\]", network)
    return a


def find_supernets(network):
    import re

    a = re.sub(r"(\[\w+\])", " ", network).split()
    return a


def find_abba(networks):
    for network in networks:
        for i in range(len(network) - 3):
            if network[i] == network[i + 3]:
                if network[i+1] == network[i+2] and network[i] != network[i+1]:
                    return True
    return False


def find_bab(networks):
    answer = []
    for network in networks:
        for i in range(len(network) - 2):
            if network[i] == network[i + 2] and network[i] != network[i+1]:
                answer.append(network[i:i+4])
    return answer


def supports_ssl(network):
    super_bab = find_bab(find_supernets(network))
    hyper_bab = find_bab(find_hypernets(network))

    for super in super_bab:
        for hyper in hyper_bab:
            if super[0] == hyper[1] and super[1] == hyper[0]:
                return True
    return False


def supports_tls(network):
    if find_abba(find_supernets(network)):
        if not find_abba(find_hypernets(network)):
            return True
    return False


def part1(input):
    total = 0
    for line in input:
        if supports_tls(line):
            total += 1

    print("Part 1:  {}".format(str(total)))


def part2(input):
    total = 0
    for line in input:
        if supports_ssl(line):
            total += 1

    print("Part 2:  {}".format(str(total)))


input = get_input()
part1(input)
part2(input)
