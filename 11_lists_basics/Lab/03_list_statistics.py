number_of_lists = int(input())
positives = []
negatives = []
for lists in range(number_of_lists):
    number = int(input())
    if number >= 0:
        positives.append(number)
    else:
        negatives.append(number)
print(f"{positives}\n{negatives}\nCount of positives: {len(positives)}\nSum of negatives: {sum(negatives)}")

