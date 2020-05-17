# Level 2.1

def validation(l, t):
    if not l or len(l)>100 or (t <1 or t >250) or sum(l)<t:
        return False
    return True

def solution(l, t):
    if not validation(l, t):
        return [-1, -1]

    summed_num = 0
    response = []

    for i, value in enumerate(l):
        if value < 1 or value > 100:
            return [-1, -1]
        for j in range(i, len(l)):
            summed_num += l[j]
            if summed_num == t:
                response.append([i, j])

        summed_num = 0

    if len(response) == 0:
        return [-1, -1]
    start_index = response[0][0]
    end_index = response[0][1]
    if start_index > end_index or len(response) == 0:
        return [-1, -1]

    return response[0]

print(solution([4, 3, 10, 2, 8], 20))