A, B = map(int, input().split()) # 요리 시작 시간 (시 분)
C = int(input()) # 요리하는 시간

A = A + C // 60
B = B + C % 60

if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A -= 24
    
print(A, B)