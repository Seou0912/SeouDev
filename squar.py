# 입력을 받아 공백으로 분리하여 a,b 에 넣는다
a, b = map(int, input().strip().split(' '))

for _ in range(b): 
# `b`번 반복하는 반복문입니다.
# - `_`는 반복 횟수를 나타내는 변수이지만, 사용하지 않는 경우 관례적으로 `_`를 사용
    print("*" *a)
    
 # ---------------------------------------------------   
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)

# --------------------------------------------------- 
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end='')
    print('')
    
# --------------------------------------------------- 
a, b = map(int, input().strip().split(' '))
print(("*" * a + "\n") * b)

# --------------------------------------------------- 
n, m = [int(x) for x in input().split()[:2]]   
print('\n'.join(['*' * n] * m))  # '\n'과 연결한 리스트를 하나의 문자열로 만듬