"""
    글자 이어 붙여 문자열 만들기
    문제 설명
    문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

    제한사항
    1 ≤ my_string의 길이 ≤ 1,000
    my_string의 원소는 영소문자로 이루어져 있습니다.
    1 ≤ index_list의 길이 ≤ 1,000
    0 ≤ index_list의 원소 < my_string의 길이
"""
def solution(my_string, index_list):
        answer = ""
        for i in index_list:
            answer += my_string[i]
        return answer
    
"""
    문자열이나 숫자를 숫자로 변환하기
    문제 설명
    문자열 my_string과 정수 n이 매개변수로 주어집니다. my_string의 길이만큼 숫자로 변환하여 return 하도록 solution 함수를 완성해주세요.

    제한사항
    1 ≤ my_string의 길이 ≤ 1,000
    my_string의 원소는 영소문자로 이루어져 있습니다.
    1 ≤ n ≤ 9
"""
def solution(my_string, n):
    answer = 0
    for i in my_string:
        answer = answer * 10 + int(i)