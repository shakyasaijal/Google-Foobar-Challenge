def answer(x, y):
    x, y = int(x), int(y)
    total = 0
    while not (x == 1 and y == 1):
        if y <= 0 or x <= 0:
            return "ixpossible"
        if y == 1:
            return str(total + x - 1)
        else:
            total += int(x/y)
            x, y = y, x % y
    return str(total)

print(answer('4', '7'))