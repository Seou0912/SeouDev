def solution(arr):
    answer = []
    for num in arr:
        if not answer or num != answer[-1]:
            answer.append(num)
        
    return answer

#----------------------------------------------------------------
def solution(arr):
    answer = []
    temp=arr[:]   # temp array is used to store the last element of the array  
    for num in arr: 
        if num != temp:
            answer.append(num)
            temp=num
        print(answer)
    return answer


#----------------------------------------------------------------

def solution(arr):
    return  [arr[i] for i in range(len(arr)) if not(arr[i:i+1] == arr[i+1:i+2])]


#----------------------------------------------------------------
def solution(arr):
    answer = [arr[0]]
    for a in arr:
        if not a == answer[-1]:
            answer.append(a)

    return answer

#----------------------------------------------------------------
def no_continuous(s):
    # 함수를 완성하세요
    return [a for b,a in enumerate(s) if a!=s[b-1]] 
# `enumerate` 함수를 사용하면 반복문을 수행할 때 인덱스를 따로 변수로 지정할 필요가 없음.

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))