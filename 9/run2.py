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

xs = sorted(list(set([x[0] for x in lines])))
ys = sorted(list(set([x[1] for x in lines])))

# 离散化
xid = {x: i for i, x in enumerate(xs)}
yid = {y: i for i, y in enumerate(ys)}

# 新建地图
mp = [[0] * len(ys) for _ in range(len(xs))]

# 重新给 lines 编号
g = []
for i in range(n):
    g.append([xid[lines[i][0]], yid[lines[i][1]]])
    mp[g[i][0]][g[i][1]] = 2

# ?
g.append(g[0])

# 沿着边染色
for i in range(n):
    if g[i][0] == g[i+1][0]:
        for j in range(min(g[i][1], g[i+1][1]), max(g[i][1], g[i+1][1]) + 1):
            if mp[g[i][0]][j] == 0:
                mp[g[i][0]][j] = 1
    else:
        for j in range(min(g[i][0], g[i+1][0]), max(g[i][0], g[i+1][0]) + 1):
            if mp[j][g[i][1]] == 0:
                mp[j][g[i][1]] = 1

# 以 94985,51083 为起点，洪水染色

# 新建队列
import queue

q = queue.Queue()
q.put((xid[94985], yid[51083]))
# q.put((xid[9], yid[3]))

while not q.empty():
    fst = q.get()
    x, y = fst
    if mp[x][y] != 0:
        continue
    mp[x][y] = 1
    q.put((x+1, y))
    q.put((x-1, y))
    q.put((x, y+1))
    q.put((x, y-1))

# 输出地图
for i in range(len(mp)):
    print(''.join(['#' if x == 2 else 'X' if x == 1 else '.' for x in mp[i]]))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        fg = True
        for x in range(min(g[i][0], g[j][0]), max(g[i][0], g[j][0]) + 1):
            for y in range(min(g[i][1], g[j][1]), max(g[i][1], g[j][1]) + 1):
                if mp[x][y] == 0:
                    fg = False
                    break
            if fg == False:
                break
        if fg:
            tmp = (abs(lines[i][0] - lines[j][0]) + 1) * (abs(lines[i][1] - lines[j][1]) + 1)
            if tmp > ans:
                ans = max(ans, tmp)
                print(lines[i], lines[j], g[i], g[j])
print(ans)