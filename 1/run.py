lines = open('input.txt').read().strip().split('\n')

x = 50
ans = 0
for line in lines:
    if line[0] == 'L':
        for _ in range(int(line[1:])):
            x -= 1
            if x % 100 == 0:
                ans += 1
    else:
        for _ in range(int(line[1:])):
            x += 1
            if x % 100 == 0:
                ans += 1
    
print(ans)
