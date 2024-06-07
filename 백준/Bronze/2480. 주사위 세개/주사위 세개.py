A, B, C = map(int, input().split())
money = 0

if (A == B) and (B == C):
    money = 10000 + (A * 1000)
elif A == B:
    money = 1000 + (A * 100)
elif A == C:
    money = 1000 + (A * 100)
elif B == C:
    money = 1000 + (B * 100)
else:
    money = max(A, B, C) * 100 # 예약어를 변수에 할당 시 에러
    
print(money)