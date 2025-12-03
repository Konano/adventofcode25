lines = open('input.txt').read().strip().split('\n')

ans = 0
for line in lines:
    s = ''
    t = -1
    for o in range(12, 0, -1):
        t += 1
        for i in range(t+1, len(line)-o+1):
            if line[i] > line[t]:
                t = i
        s += line[t]
    ans += int(s)
print(ans)