chess = [1, 1, 2, 2, 2, 8]
chess_present = list(map(int, input().split()))

for i in range(0, 6):
    print(chess[i] - chess_present[i], end = ' ')