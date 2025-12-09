lines = open('input.txt').read().strip().split('\n')
lines = [[int(y) for y in x.split(',')] for x in lines]
n = len(lines)

# mp = [list(x) for x in open('input.txt').read().strip().splitlines()]
# n, m = len(mp), len(mp[0])


def dis(i, j):
    # 迪杰斯特拉距离
    return (lines[i][0] - lines[j][0]) ** 2 + (lines[i][1] - lines[j][1]) ** 2 + (lines[i][2] - lines[j][2]) ** 2


q = []
for i in range(n):
    for j in range(i+1, n):
        q.append((dis(i, j), i, j))

q.sort()

h = [i for i in range(n)]

# 并查集
def find(x):
    if h[x] != x:
        h[x] = find(h[x])
    return h[x]

count = n
for x in range(len(q)):
    d, i, j = q[x]
    hi, hj = find(i), find(j)
    if hi != hj:
        h[hi] = hj
        count -= 1
        if count == 1:
            print(lines[i], lines[j])
            print(lines[i][0] * lines[j][0])
            break
    # print(f"{lines[i]} <-> {lines[j]}: {d ** 0.5:.2f}")

# 统计并查集大小
cnt = {}
for i in range(n):
    hi = find(i)
    if hi not in cnt:
        cnt[hi] = 0
    cnt[hi] += 1

# 统计最大的三个
res = sorted(cnt.values(), reverse=True)[:3]
print(res)
print(res[0] * res[1] * res[2])
