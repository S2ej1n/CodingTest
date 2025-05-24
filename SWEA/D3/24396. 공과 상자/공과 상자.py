#B상자에 검은공 X, W상자에 흰공 Y, 서로 바뀌면 Z
#합이 최대

#검은 상자에 검은공 개수 bb * X, 흰 상자에 흰 공 개수 ww * Y
#검은 공의 남은 개수 (B-bb)* Z, (W-ww)*Z
def max_score( B, W, X, Y, Z ):
    max_total = float('-inf')
    
    for Bb in range(B +1):
        for Ww in range(W+1):
            # 검은 상자 검은공이랑/ 검은상자에 들어갈 흰공이 , 검은상자 크기보다 크면 안됨.
            if Bb + (W - Ww) > B or Ww + (B - Bb) > W:
                continue
            
            sumresult = (Bb * X) + (Ww * Y) + (B-Bb)* Z + (W-Ww)*Z
            max_total = max(max_total,sumresult)
    return max_total

T = int(input())

for test_case in range(1, T + 1):
    B, W, X, Y, Z = map(int, input().split())
    print(max_score( B, W, X, Y, Z ))
    
