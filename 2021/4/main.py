s = open("input.txt").read().split()
draws = s.pop(0).split(",")
boards = [[x[j*5:(j+1)*5] for j in range(5)] for x in [s[i*25:(1+i)*25] for i in range(len(s) // 25)]]

def unmarked(board, draw):
    return sum(int(i) for j in board for i in j if i not in draw)

def win(board, draw, t=False):
    for i in range(5):
        if all(j in draw for j in board[i]):
            return unmarked(board, draw) * int(draw[-1])
    if all(board[j][j] in draw for j in range(5)):
        return unmarked(board, draw) * int(draw[-1])
    return win(list(zip(*board)), draw, True) if not t else 0

def solve1():
    for i in range(len(draws)):
        for j in boards:
            if win(j, draws[:i]):
                print(win(j, draws[:i]))
                return

def solve2(boards):
    d = []
    while len(boards) != 0:
        d.append(draws.pop(0))
        for b in boards:
            if win(b, d):
                boards.remove(b)
    print(win(b, d))

solve1()
solve2(boards)
