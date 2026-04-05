'''
길이 1이상 도로 구간, 모든 물체수 3배수


'''
import sys
input = sys.stdin.readline

N = int(input())
road = input().strip()

check = {'T':0, 'G':0, 'F':0, 'P':0}
# 해당 상태가 지금까지 몇번 나왔는고?
how_letter_appear= {}
how_letter_appear[(0,0,0,0)] = 1
# print(how_letter_appear)

answer = 0

for r in road:
    check[r] += 1
    # print(r)
    # print(check)

    key = (check['T']%3, check['G']%3, check['F']%3, check['P']%3)

    if key in how_letter_appear:
        # print('[28]',how_letter_appear)
        answer += how_letter_appear[key]
        # print('answer : ',answer)
        how_letter_appear[key] += 1
        # print('[32]',how_letter_appear)
    else:
        how_letter_appear[key] = 1

print(answer)