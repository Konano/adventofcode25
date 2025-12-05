lines = open('input.txt').read().strip().split('\n')
# mp = [list(x) for x in open('input.txt').read().strip().splitlines()]

ans = 0

rgs = []
for x in lines:
    if '-' in x:
        a, b = x.split('-')
        rgs.append((int(a), int(b)))
    elif len(x):
        for k in range(len(rgs)):
            a, b = rgs[k]
            if a <= int(x) <= b:
                ans += 1
                break

print(ans)

p = []
for x in range(len(rgs)):
    p.append((rgs[x][0], 's'))
    p.append((rgs[x][1]+1, 'e'))
p.sort()

ans = 0
cnt = 0
pre_x = -1
for x in p:
    ans += max(0, x[0]-pre_x) * (cnt > 0)
    if x[1] == 's':
        cnt += 1
    else:
        cnt -= 1
    pre_x = x[0]

print(ans)
