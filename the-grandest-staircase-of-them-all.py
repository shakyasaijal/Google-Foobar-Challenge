# level 3.1

def validation(n):
    if n < 3 or n > 200:
        return False
    return True


def solution(n):
    if not validation(n):
        return 0

    size = n + 1
    matrix = [[0 for _ in xrange(size)] for _ in xrange(size)]
    matrix[0][0] = 1
    for prev in xrange(1, size):
        for left in xrange(0, size):
            matrix[prev][left] = matrix[prev-1][left]
            if left >= prev:
                matrix[prev][left] += matrix[prev - 1][left - prev]
    return matrix[n][n] - 1
