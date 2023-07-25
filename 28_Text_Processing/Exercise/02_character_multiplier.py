string1, string2 = input().split()
summ = 0
if len(string1) > len(string2):
    for idx in range(len(string2)):
        summ += ord(string1[idx]) * ord(string2[idx])

    for idx in range(len(string2), len(string1)):
        summ += ord(string1[idx])

elif len(string2) > len(string1):
    for idx in range(len(string1)):
        summ += ord(string2[idx]) * ord(string1[idx])

    for idx in range(len(string1), len(string2)):
        summ += ord(string2[idx])

else:
    for idx in range(len(string1)):
        summ += ord(string2[idx]) * ord(string1[idx])

print(summ)
