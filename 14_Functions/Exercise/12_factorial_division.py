def muriel(number: int) -> int:
    result = 1
    for cowrage in range(1, number + 1):
        result *= cowrage
    return result


entry_one = int(input())
entry_two = int(input())
print(f'{muriel(entry_one) / muriel(entry_two):.2f}')
