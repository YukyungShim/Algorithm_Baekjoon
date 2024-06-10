num = []

for i in range(9):
    j = int(input())
    num.append(j)
    
print(max(num))
print(num.index(max(num))+1)