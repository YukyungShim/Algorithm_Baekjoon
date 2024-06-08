T = int(input())

for x in range(T):
    A, B = map(int, input().split())
    C = A + B
    print(f"Case #{x+1}:", f"{A} + {B} =", C)