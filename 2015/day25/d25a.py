current_val = 20151125
end_row = 2947
end_col = 3029

for i in range(2, 10000):
    for a in range(i, 0, -1):
        b = i - a + 1
        current_val = (current_val * 252533) % 33554393
        if a == end_row:
            if b == end_col:
                print(str(a)+"-"+str(b)+"-"+str(current_val))
                exit()
