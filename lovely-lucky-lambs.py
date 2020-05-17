# Level 2.2


def solution(total_lambs):
    try:
        int(total_lambs)
    except Exception:
        return 0
    if total_lambs > 10**9 or not total_lambs or total_lambs < 1:
        return 0

    value = []
    flag = 0
    x = 1
    # Powered by x
    while x < total_lambs:
        current_value = 2**x
        value.append(current_value)
        flag += current_value
        x += 1
        if flag > total_lambs:
            break

    # Fibonacci
    n1 = 1
    n2 = 1
    total = 0
    fibo = 0
    while total + n1 <= total_lambs:
        total += n1
        n1, n2 = n2, n1 + n2
        fibo += 1
    return int(fibo - len(value))
