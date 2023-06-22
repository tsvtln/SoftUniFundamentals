lines = [int(x) for x in input().split(', ')]
print(f"Positive: {', '.join(str(x) for x in lines if x >= 0)}")
print(f"Negative: {', '.join(str(x) for x in lines if x < 0)}")
print(f"Even: {', '.join(str(x) for x in lines if x % 2 == 0)}")
print(f"Odd: {', '.join(str(x) for x in lines if x % 2 != 0)}")
