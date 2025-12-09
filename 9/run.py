lines = open('input.txt').read().strip().split('\n')
lines = [[int(y) for y in x.split(',')] for x in lines]
n = len(lines)

# mp = [list(x) for x in open('input.txt').read().strip().splitlines()]
# n, m = len(mp), len(mp[0])

# ans = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         ans = max(ans, abs(lines[i][0] - lines[j][0] + 1) * abs(lines[i][1] - lines[j][1] + 1))
# print(ans)

ans = 0

i0 = 248
for i in range(n):
    if i != i0 and lines[i0][1] <= lines[i][1] <= 68048:
        ans = max(ans, (abs(lines[i0][0] - lines[i][0]) + 1) * (abs(lines[i0][1] - lines[i][1]) + 1))

i1 = 249
for i in range(n):
    if i != i1 and 34491 <= lines[i][1] <= lines[i1][1]:
        ans = max(ans, (abs(lines[i1][0] - lines[i][0]) + 1) * (abs(lines[i1][1] - lines[i][1]) + 1))

print(ans)