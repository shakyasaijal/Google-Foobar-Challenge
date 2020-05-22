def solution(n):
    if n < 0 or n > 10000:
        return 0

    prime_numbers = ""
    for x in range(1, n+100):
        if x > 1:
            for i in range(2, x):
                if(x % i == 0):
                    break
            else:
                prime_numbers += str(x)

    return prime_numbers[n:n+5]
