# lines = open('input.txt').read().strip().split('\n')
# mp = [[y for y in x.split() if y] for x in open('input.txt').read().strip().splitlines()]

# ans = 0
# for i in range(1000):
#     if mp[-1][i] == '+':
#         x = 0
#         for k in range(4):
#             x += int(mp[k][i])
#         ans += x
#     else:
#         x = 1
#         for k in range(4):
#             x *= int(mp[k][i])
#         ans += x

# print(ans)


lines = open('input.txt').read().split('\n')

ans = 0
p = []
for i in range(len(lines[0])-1, -1, -1):
    if all(line[i] == ' ' for line in lines):
        continue
    p.append(int(''.join([lines[o][i] for o in range(4)]).strip()))
    if lines[-1][i] in ['+', '*']:
        if lines[-1][i] == '+':
            ans += sum(p)
        else:
            x = 1
            for v in p:
                x *= v
            ans += x
        p = []
print(ans)
