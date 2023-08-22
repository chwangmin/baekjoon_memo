"""
1. 문자열과 폭발 단어를 입력 받는다.
2. 마지막 bomb의 문자와 길이를 입력받는다.
3. stack을 만든다.
4. 문자열에서 하나씩 문자를 뽑습니다.
5. stack의 top의 문자가 bomb의 마지막 문자와 같다면, 
    stack에서 bomb의 문자열 길이 만큼 뺀 문자열과 bomb 문자열이 같은지 확인 후 같으면 stack에서 삭제
6. 마지막에 ''.join(stack)을 사용해서 연결된 문자열로 치환 후 출력
    만약에 stack에 값이 없다면 'FRULA'
"""

string = input()
bomb = input()

lastChar = bomb[-1]
length = len(bomb)
stack = []

for s in string:
    stack.append(s)
    if s == lastChar and ''.join(stack[-length:]) == bomb:
        del stack[-length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)