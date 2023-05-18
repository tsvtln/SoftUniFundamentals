from re import findall
text, wc = input(), 0
text = str.lower(text)

pat1, pat2, pat3, pat4 = 'sand', 'water', 'fish', 'sun'

count1 = len(findall(pat1, text))
count2 = len(findall(pat2, text))
count3 = len(findall(pat3, text))
count4 = len(findall(pat4, text))

print(count1 + count2 + count3 + count4)
