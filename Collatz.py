def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(78))

def solution(num):

    answer = 0
    while num !=1:
        if num % 2 ==0:
            num = num // 2
        else :
            num = num * 3 + 1
        answer += 1
        
        if answer ==500:
            return -1
    return answer



def solution(num):
    for i in range(199):
        if num == 1: return i
        num = num * 3 + 1 if num & 1 else num >> 1;
    return -1;