words = []

for i in range(5):
    word = input().strip()
    words.append(word)
    
result = "" # 세로로 읽은 문자열을 저장할 변수

max_len = max(len(word) for word in words)

# 가장 긴 문자열의 길이만큼 반복
for i in range(max_len):
    for j in range(5):
        if i < len(words[j]):
            result += words[j][i]
            
print(result)