wrd = input()
index = []
for i in range(len(wrd)):
    if wrd[i].isupper():
        index.append(i)
print(index)
    