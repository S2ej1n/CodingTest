def solution(board, moves):
    baket = []
    answer = 0
    
    for move in moves:
        col = move-1 #세로(보드에서 갖고나올거)
        
        for k in range(len(board)):
            if board[k][col] != 0:
                pick = board[k][col]
                board[k][col] = 0
                
                if baket and baket[-1] == pick:
                    baket.pop()
                    answer += 2
                else:
                    baket.append(pick)
                break
    return answer