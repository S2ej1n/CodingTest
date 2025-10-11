def solution(n):
    fi = [0,1]
    for n in range(2,n+1):
        fin = fi[n-1] + fi[n-2]
        fi.append(fin)
    answer = fi[n]%1234567
    return answer