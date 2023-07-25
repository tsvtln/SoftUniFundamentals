find_file = input().split("\\")
for word in find_file:
    if '.' in word:
        file = word.split('.')
        print(f"File name: {file[0]}\nFile extension: {file[1]}")
