MONKEYS = {}


class Monkey:
    def __init__(self, items, operation, ops_value, test_divsor, true_monkey, false_monkey):
        self.items = items
        self.operation = operation
        self.ops_value = ops_value
        self.test_divsor = test_divsor
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0

    def add_item(self, item):
        self.items.append(item)

    def inspect_items(self, round2=False):
        for item in self.items:
            if self.ops_value == "old":
                the_value = item
            else:
                the_value = self.ops_value
            if self.operation == "*":
                worry = item * the_value
            else:
                worry = item + the_value

            if not round2:
                worry = worry // 3

            if worry % self.test_divsor == 0:
                MONKEYS[self.true_monkey].add_item(worry)
            else:
                MONKEYS[self.false_monkey].add_item(worry)
            self.inspections += 1
        self.items = []

    def get_inspections(self):
        return self.inspections


def get_input():
    from os import path

    with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
        for line in f:
            line = line.strip()

            if line.startswith("Monkey"):
                monkey_num = int(line.split()[1][:-1])
            elif line.startswith("Starting"):
                line = line.split(":")
                items = [int(i) for i in line[1].replace(",", "").split()]
            elif line.startswith("Operation"):
                line = line.split()
                operation = line[4]
                if line[5] == "old":
                    ops_value = "old"
                else:
                    ops_value = int(line[5])
            elif line.startswith("Test"):
                test_divsor = int(line.split()[3])
            elif "true" in line:
                true_monkey = int(line.split()[5])
            elif "false" in line:
                false_monkey = int(line.split()[5])
            else:
                monkey = Monkey(items, operation, ops_value,
                                test_divsor, true_monkey, false_monkey)
                MONKEYS[monkey_num] = monkey
        monkey = Monkey(items, operation, ops_value,
                        test_divsor, true_monkey, false_monkey)
        MONKEYS[monkey_num] = monkey


def part1():
    keys = MONKEYS.keys()
    for i in range(20):
        for key in keys:
            the_monkey = MONKEYS[key]
            the_monkey.inspect_items()

    inspections = []
    for key in keys:
        inspections.append(MONKEYS[key].get_inspections())

    inspections = sorted(inspections, reverse=True)

    print('Part 1:  {}'.format(str(inspections[0] * inspections[1])))


def part2():
    get_input()
    keys = MONKEYS.keys()
    for i in range(10000):
        print(f"{i:,d}")
        for key in keys:
            the_monkey = MONKEYS[key]
            the_monkey.inspect_items(round2=True)

    inspections = []
    for key in keys:
        inspections.append(MONKEYS[key].get_inspections())

    inspections = sorted(inspections, reverse=True)

    print('Part 2:  {}'.format(str(inspections[0] * inspections[1])))


input = get_input()
# part1()
part2()
