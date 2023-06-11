numbers = [int(number) for number in input().split(', ')]
indices = []
for idx, ele in enumerate(numbers):
    if ele % 2 == 0:
        indices.append(idx)

print(indices)
