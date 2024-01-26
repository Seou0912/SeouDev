#"comprehension"
# list, dict르ㄹ 쉽게 만들어줌

numbers = range(1, 10)

sqaure_numbers = []

for number in numbers:
    sqaure_numbers.append(number**2)

# sqaure_numbers2 = [number ** 2  for number in numbers]
sqaure_numbers2 = [number**2 for number in numbers if number % 2 != 0]
# print(sqaure_numbers)
# print(sqaure_numbers2)


score = [["최지헌", 90], ["정서우", 100], ["김땡땡", 87]]

name_with_score = {s[0]: s[1] for s in score if s[1] > 50}

print(name_with_score)

# Lambda

def a(x,y):
    return z+y

a(x=1,y=2)

lambda x,y:x+y 