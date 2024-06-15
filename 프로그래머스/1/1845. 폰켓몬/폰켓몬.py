def solution(nums):
    pick = len(nums)//2
    count = len(set(nums))
    
    if pick < count:
        answer = pick
    else:
        answer = count
    return answer