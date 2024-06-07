H, M = map(int, input().split())

if M >= 45:
    M = M - 45
    print(H, M)
elif (H > 0) and (M < 45):
    H = H - 1
    M2 = (60 + M) - 45
    print(H, M2)
else: # H = 0
    H2 = (H + 24) -1
    M2 = (60 + M) - 45
    print(H2, M2)