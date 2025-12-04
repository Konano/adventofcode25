mp = [list(x) for x in open('input.txt').read().strip().splitlines()]

ans = 0
remove = True
while remove:
    remove = False
    for x in range(len(mp)):
        for y in range(len(mp[0])):
            if mp[x][y] == '@':
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(mp) and 0 <= ny < len(mp[0]):
                            if mp[nx][ny] != '.':
                                count += 1
                if count < 4:
                    mp[x][y] = 'X'
                    remove = True
    for x in range(len(mp)):
        for y in range(len(mp[0])):
            if mp[x][y] == 'X':
                mp[x][y] = '.'
                ans += 1
                
print(ans)