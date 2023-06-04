def calculate(operator: str, integer_one: int, integer_two: int) -> int:
    if operator == 'multiply':
        result = integer_one * integer_two
        return result
    elif operator == 'divide':
        result = integer_one // integer_two
        return result
    elif operator == 'add':
        result = integer_one + integer_two
        return result
    elif operator == 'subtract':
        result = integer_one - integer_two
        return result


inp_operator = input()
value_one = int(input())
value_two = int(input())

print(calculate(inp_operator, value_one, value_two))
