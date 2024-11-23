import sys

n = int(input())
obstacles = [[int(num) for num in input().split()] for i in range(n)]
obstacles.sort()

max_obstacle = [-1, 0]
max_obstacle_index = -1
second_max = [-1, 0]
second_max_index = -1
for i in range(n):
    if obstacles[i][1] > obstacles[i][0]:
        print(-1)
        sys.exit(0)
    if obstacles[i][1] > max_obstacle[1]:
        max_obstacle = obstacles[i]
        max_obstacle_index = i
        second_max = [-1, 0]
        second_max_index = -1
    elif obstacles[i][1] > second_max[1]:
        second_max = obstacles[i]
        second_max_index = i


result = max_obstacle[1] + max_obstacle[0]
if second_max_index > 0:
    result += obstacles[-1][0] - second_max[0] - (max_obstacle[1] - second_max[1])
for i in range(second_max_index + 1, n):
    result += obstacles[i][0] - obstacles[i - 1][0] - (obstacles[i][1] - obstacles[i - 1][1])
print(result)
# result = 2 * max_obstacle[1] + max_obstacle[0] - max_obstacle[1]