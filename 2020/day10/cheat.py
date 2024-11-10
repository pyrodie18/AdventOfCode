from math import prod
ratings = sorted(map(int, open('./Day10/D10_Input.txt').readlines()))
ratings = [0] + ratings + [ratings[-1] + 3]
print(prod(map(sum, zip(*((b - a == 1, b - a == 3) for a, b in zip(ratings, ratings[1:]))))))