n = int(input())
stick_len = [int(num) for num in input().split()]
stick_len.sort(reverse=True)
result = 0
for i in range(0, n - (n % 4), 4):
    result += stick_len[i + 1] * stick_len[i + 3]
print(result)
