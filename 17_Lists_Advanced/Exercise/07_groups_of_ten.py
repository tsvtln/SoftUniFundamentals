sequence = [int(x) for x in input().split(', ')]
group_num = 10
while len(sequence) > 0:
    group_list = []
    for number in sequence:
        if number <= group_num:
            group_list.append(number)
    print(f"Group of {group_num}'s: {group_list}")
    for number in group_list:
        if number in sequence:
            sequence.remove(number)
    group_num += 10


