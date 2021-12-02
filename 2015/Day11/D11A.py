bad_letters = [105, 108, 111]  
start_value = [103, 104, 105, 106, 107, 108, 109, 110]

a = 99
b = 113
c = 106
d = 120
e = 106
f = 110
g = 100
h = 115

start_passed = False

def check_password (letters):
    valid_password = False
    for letter in letters:
        if letter in bad_letters:
            return valid_password

    series = False
    for i in range (5):
        if letters[i] + 1 == (letters[i+1]) and letters[i] + 2 == (letters[i+2]):
            series = True
            break
    if not series:
        return valid_password
    double1 = False
    double2 = False
    for i in range (0, 5):
        if letters[i] == letters[i+1]:
            double1 = True
            break
    for j in range (i+2, 7):
        if letters[j] == letters[j+1]:
            double2 = True
            break
    if double1 and double2:
        valid_password = True
    return valid_password

while a < 122:
    while b < 122:
        while c < 122:
            while d < 122:
                while e < 122:
                    while f < 122:
                        while g < 122:
                            while h < 122:
                                if check_password([a, b, c, d, e, f, g, h]):
                                    print(chr(a)+chr(b)+chr(c)+chr(d)+chr(e)+chr(f)+chr(g)+chr(h))
                                    exit()
                                else:
                                    h += 1
                            h = 97
                            g += 1
                        g = 97
                        f += 1
                    f = 97
                    e += 1
                e = 97
                d += 1
            d = 97
            c += 1
        c = 97
        b += 1
    b = 97
    a += 1
