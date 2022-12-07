from sys import maxsize


# legend ["walk", "bike", "train", "car"]
# get lowest time, and if tie lowest money cost mode of transport, from source to destination

def getStartEnd(grid):
    s, e = None, None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                s = (i, j)
            elif grid[i][j] == "D":
                e = (i, j)
    return s, e


def getBestModeOfTransport(grid, time, money):
    if not grid or not time or not money:
        return

    n, m = len(grid), len(grid[0])
    s, e = getStartEnd(grid)
    if not s or not e:
        return

    def inBounds(i, j):
        nonlocal n, m
        return 0 <= i < n and 0 <= j < m

    def explore(i, j, hops, typ):
        nonlocal grid, adj, seen, bestTime, bestCost, mode
        seen.add((i, j))

        if grid[i][j] == "D":
            timeCost = hops * time[int(typ) - 1]
            moneyCost = hops * money[int(typ) - 1]
            if timeCost < bestTime or (timeCost == bestTime and moneyCost < bestCost):
                bestTime = timeCost
                bestCost = moneyCost
                mode = typ

        for ii, jj in adj:
            y, x = i + ii, j + jj
            if not inBounds(y, x) or (y, x) in seen or \
                    (grid[y][x] != typ or grid[y][x] != "D"):
                continue
            seen.add((y, x))
            explore(y, x, hops + 1, typ)

    adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    seen = {s}
    bestTime, bestCost, mode = maxsize, maxsize, None

    for ii, jj in adj:
        y, x = ii + s[0], jj + s[1]
        if not inBounds(y, x):
            continue
        seen.add((y, x))
        explore(y, x, 1, grid[y][x])

    return mode


