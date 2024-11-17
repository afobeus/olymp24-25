t = int(input())
numbers = map(int, input().split())
for n in numbers:
    path_len = 1
    max_number = n

    while n != 1:
        path_len += 1
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        max_number = max(max_number, n)

    print(path_len, max_number)
