n = int(input())
for _ in range(n):
    v1, k1, r1, v2, k2, r2, t = map(int, input().split())
    vasya_dist = v1 * k1 * (t // (k1 + r1)) + v1 * min(k1, (t % (k1 + r1)))
    petya_dist = v2 * k2 * (t // (k2 + r2)) + v2 * min(k2, (t % (k2 + r2)))
    if vasya_dist > petya_dist:
        print("Vasya")
    elif petya_dist > vasya_dist:
        print("Petya")
    else:
        print("Draw")
