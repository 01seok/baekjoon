'''
문자열 뒤에 A를 추가한다.
문자열을 뒤집고 뒤에 B를 추가한다.
반대로 뒤집어서 생각해보기
'''
S = input()
T = input()

while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1][::-1]

if S == T:
    print(1)
else:
    print(0)