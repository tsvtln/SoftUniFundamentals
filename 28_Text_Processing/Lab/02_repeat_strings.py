string = input().split()
for print_strings in range(len(string)):
    print(f"{string[print_strings] * len(string[print_strings])}", end='')
