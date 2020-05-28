def validation(l):
    if len(l) < 2 or len(l) > 2000 or min(l) < 1 or max(l) > 999999:
        return False
    return True


def solution(l):
    if not validation(l):
        return 0

    cnt = 0
    for i in range(1, len(l) - 1):
        cnt_x = len([x for x in l[:i] if l[i] % x == 0])
        cnt_z = len([z for z in l[i + 1:] if z % l[i] == 0])

        cnt += cnt_x * cnt_z
    return cnt


print(solution([1, 2, 3, 4, 5, 6]))
