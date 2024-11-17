n, m, k = map(int, input().split())
allowed_before = [list(range(10)) for _ in range(10)]
nums = map(int, input().split())
for num in nums:
    allowed_before[num % 10].pop(allowed_before[num % 10].index(num // 10))
prohibited_numbers = [set() for _ in range(n)]
for i in range(k):
    nums = [int(num) for num in input().split()]
    for num in nums[2:]:
        prohibited_numbers[nums[0]].add(num)

dp = [[0 for j in range(10)] for i in range(n)]
for i in range(10):
    dp[0][i] = 1
for i in prohibited_numbers[0]:
    dp[0][i] = 0

for i in range(1, n):
    for j in range(10):
        if j in prohibited_numbers[i]:
            continue
        for p in allowed_before[j]:
            dp[i][j] += dp[i - 1][p]

print(sum(dp[n - 1][1:]))
