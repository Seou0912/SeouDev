def check_bomb(code):
    # 코드를 숫자로 변환하는 딕셔너리
    numbers = {
        "***   * *** *** *** *** *** ***": "0",
        "  *   *   *   * * * * * * * * *": "1",
        "***   * *** *** *** *** *** ***": "2",
        "***   * *** *** *** *** *** ***": "3",
        "* *   * * * ***   * *** *** ***": "4",
        "*** * *** ***   * *** *** ***": "5",
        "*** * *** ***   * *** *** ***": "6",
        "***   *   *   *   *   *   *   *": "7",
        "***   * *** *** * *** *** ***": "8",
        "***   * *** *** * *** *** ***": "9",
    }

    # 코드를 숫자로 변환
    code_number = ""
    for i in range(0, len(code), 5):
        code_part = code[i : i + 5]
        if code_part in numbers:
            code_number += numbers[code_part]
        else:
            return "BOOM!!"

    # 코드 숫자가 6으로 나누어 떨어지는지 확인
    if int(code_number) % 6 == 0:
        return "BEER!!"
    else:
        return "BOOM!!"


# 입력 받기
code = []
for _ in range(5):
    line = input()
    code.append(line)

# 폭탄 해체 여부 출력
result = check_bomb(code)
print(result)
