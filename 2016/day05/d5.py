SEED = "ffykfhsq"
PREFIX = "00000"


def part1():
    import hashlib
    answer1 = []
    answer2 = ["!"] * 8
    i = 0
    while True:
        hash = (SEED + str(i)).encode('utf8')
        result = hashlib.md5(hash)
        if result.hexdigest().startswith(PREFIX):
            print(i)
            if len(answer1) <= 7:
                answer1.append(str(result.hexdigest())[5])
                print(answer1)

            if str(result.hexdigest())[5].isdigit():
                if int(str(result.hexdigest())[5]) <= 7 and answer2[int(str(result.hexdigest())[5])] == "!":
                    answer2[int(str(result.hexdigest())[5])] = str(
                        result.hexdigest())[6]
                    print(answer2)

            if len(answer1) == 8 and "!" not in answer2:
                break

        i += 1

    print("Part 1:  {}".format("".join(answer1)))
    print("Part 2:  {}".format("".join(answer2)))


part1()
