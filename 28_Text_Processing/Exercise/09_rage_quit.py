text = input().upper()
unique_symbols = ""
current_symbol = ""
repetitions = ""
for index in range(len(text)):
    if not text[index].isdigit():
        current_symbol += text[index]
    else: # text[index] is digit -> working with repetitions
        for next_symbols_index in range(index,len(text)):
            if not text[next_symbols_index].isdigit():
                break
            repetitions += text[next_symbols_index]
        unique_symbols += current_symbol * int(repetitions)
        current_symbol = ""
        repetitions = ""
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(unique_symbols)

# entry = input()
# final_string = ''
# letters = ''
# number = 0
# number_ = ''
# unique_symbols = 0
# unique_symbols_ = ''
# FLAG = False
# for char in entry:
#     if char.isalpha() or not char.isdigit():
#         if FLAG:
#             number = int(number_)
#             final_string += letters * number
#             letters = ''
#             FLAG = False
#         if char.isalpha():
#             letters += char.upper()
#             number_ = ''
#         else:
#             letters += char
#             number_ = ''
#     elif char.isdigit():
#         number_ += char
#         FLAG = True
#     if char == entry[-1]:
#         number = int(number_)
#         final_string += letters * number
#
#
# for char in final_string:
#     if char not in unique_symbols_:
#         unique_symbols_ += char
#         unique_symbols += 1
#
# print(f"Unique symbols used: {unique_symbols}\n{final_string}")
