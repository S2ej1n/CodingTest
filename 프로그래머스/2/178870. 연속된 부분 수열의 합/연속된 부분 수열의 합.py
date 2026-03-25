'''
정렬된 수열이므로 k보다 큰경우와 작은경우를 본다~!
- 합이 k보다 작으면 right 증가 → 범위 확장
- 합이 k보다 크면 left 증가 → 범위 축소
'''
def solution(sequence, k):
    left = 0
    right = 0
    curr_sum = sequence[0]
    answer = [0, len(sequence)-1]
    
    while left < len(sequence) and right < len(sequence):
        if curr_sum == k:
            # 구간 길이 비교
            if (answer[1]-answer[0]) > right - left:
                answer = [left, right]
        
        if curr_sum < k:
            right += 1
            if right < len(sequence):
                curr_sum += sequence[right]
        else:
            curr_sum -= sequence[left]
            left += 1
            
    return answer