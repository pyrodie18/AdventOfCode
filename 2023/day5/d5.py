def get_input():
    from os import path

    input = {}

    buffer = []
    section = None

    for line in reversed(list(open(path.join(path.dirname(__file__), 'input.txt')))):
        line = line.strip()

        # Blank line
        if line == "":
            input[section] = buffer
            buffer = []
        elif "map" in line:
            section = line.split()[0]
        elif line[0].isdigit():
            buffer.append([int(i) for i in line.split()])
        # Get the seeds info
        elif line.startswith("seeds"):
            line = line.split(":")
            seeds = [int(i) for i in line[1].split()]
            input["seeds"] = seeds
    return input


def find_match(input_val, maps):
    for map in maps:
        start = map[1]
        end = start + map[2] - 1
        if start <= input_val and input_val <= end:
            return map[0] + (input_val - start)
    return input_val


def part1(input):
    answer = 10000000000
    for seed in input["seeds"]:
        # Find the Soil
        soil = find_match(seed, input["seed-to-soil"])
        fertilizer = find_match(soil, input["soil-to-fertilizer"])
        water = find_match(fertilizer, input["fertilizer-to-water"])
        light = find_match(water, input["water-to-light"])
        temp = find_match(light, input["light-to-temperature"])
        humidity = find_match(temp, input["temperature-to-humidity"])
        location = find_match(humidity, input["humidity-to-location"])
        if location < answer:
            answer = location

    print("Part 1:  {}".format(str(answer)))


def part2(input):
    answer = 10000000000
    for i in range(0, len(input["seeds"]), 2):
        start = input["seeds"][i]
        end = start + input["seeds"][i + 1]
        for j in range(start, end):
            # Find the Soil
            soil = find_match(j, input["seed-to-soil"])
            fertilizer = find_match(soil, input["soil-to-fertilizer"])
            water = find_match(fertilizer, input["fertilizer-to-water"])
            light = find_match(water, input["water-to-light"])
            temp = find_match(light, input["light-to-temperature"])
            humidity = find_match(temp, input["temperature-to-humidity"])
            location = find_match(humidity, input["humidity-to-location"])
            if location < answer:
                answer = location

    print("Part 1:  {}".format(str(answer)))


input = get_input()
# part1(input)
part2(input)
