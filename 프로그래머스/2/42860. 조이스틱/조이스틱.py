'''
- 알파벳 변경 횟수는 A에서 B방향으로 이동, A에서 Z로 이동중 최솟값 선택
- 연속된 A를 찾아야함. 연속된 A길이에 따라 최소 이동 방향이 달라지므로
- 커서의 이동 횟수 = min(기존 저장값, 연속된 A를 왼쪽까지 탐색후 역으로 돌아가, 
    연속된 A의 오른쪽까지 탐색후 정방향으로 돌아가 시작)
'''
def solution(name):
    arr = list(name)
    alpha = 0
    cursor = len(name) - 1
    
    for idx, i in enumerate(arr):
        # 알파벳 변경횟수 구하기
        alpha += min(abs(ord('A') - ord(i)), abs(ord('Z') - ord(i))+1)
        
        finish = idx + 1 # i 다음부터
        # A가 끝나는 지점 찾기
        while finish < len(name) and name[finish] == 'A':
            finish += 1

        cursor = min(cursor, 
                     2 * idx + len(name) - finish,
                     idx + 2 * (len(name) - finish))

    return alpha + cursor