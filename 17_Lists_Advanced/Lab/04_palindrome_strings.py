pali_list, pali_word, found_list = [word for word in input().split()], input(), []
for word in pali_list:
    if word == word[::-1]:
        found_list.append(word)

print(f'{found_list}\nFound palindrome {pali_list.count(pali_word)} times')
