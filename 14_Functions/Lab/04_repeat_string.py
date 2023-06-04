# def multi_string(string: str, mutliplier: int) -> str:
#     return string * mutliplier


input_string = input()
input_multiplier = int(input())
# print(multi_string(input_string, input_multiplier))
repeat_string = lambda a, b: a * b
result = repeat_string(input_string, input_multiplier)
print(result)
