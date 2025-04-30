# x가 0아니면 배열에 x 추가 / 0이면 절댓값 작은거 출력
import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    x = int(sys.stdin.readline())
    if x != 0 :
        heapq.heappush(heap, (abs(x),x))
        # 튜플 - 왼쪽꺼 비교하고, 그 다음 두번째 값 비교한다.
        # 절댓값 작은거 먼저 정렬하고, 그 다음 실제값 작은거 정렬.
    else :
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])