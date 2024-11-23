n = int(input())
s = input()
letters_count = [0 for _ in range(ord('z') - ord('a') + 1)]
for i in range(n):
    letters_count[ord(s[i]) - ord('a')] += 1

full = ""
for i in range(len(letters_count)):
    if letters_count[i]:
        full += chr(ord('a') + i)
for i in range(len(full)):
    letters_count[ord(s[i]) - ord('a')] -= 1

result = 10 ** 10
for i in range(len(full), n):
    enough_letters = True
    count_operations = 0
    letters_copy = letters_count.copy()
    for j in range(len(full)):
        if s[i - len(full) + j] != full[j]:
            count_operations += 1
            letters_copy[ord(full[j]) - ord('a')] -= 1
            if letters_copy[ord(full[j]) - ord('a')] < 0:
                enough_letters = False
                break
    if enough_letters:
        result = min(result, count_operations)

if result == 10 ** 10:
    print(-1)
else:
    print(result)