# lines = open('input.txt').read().strip().split('\n')
mp = [list(x) for x in open('input.txt').read().strip().splitlines()]
n, m = len(mp), len(mp[0])

k = [0] * m
for j in range(m):
    if mp[0][j] == 'S':
        k[j] = True

ans = 0
for i in range(1, n):
    k_new = [0] * m
    for j in range(m):
        if mp[i][j] == '.' and k[j]:
            k_new[j] += k[j]
        elif mp[i][j] == '^' and k[j]:
            k_new[j] = 0
            k_new[j-1] += k[j]
            k_new[j+1] += k[j]
            ans += 1
    print(k, k_new)
    k = k_new

print(sum(k))