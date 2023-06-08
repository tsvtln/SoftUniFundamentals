def data_types(command, value):
    integer = 0
    real = 0.00
    string = ''
    if command == 'int':
        integer = value * 2
        print(integer)
    elif command == 'real':
        real = float(value) * 1.5
        print(f"{real:.2f}")
    elif command == 'string':  # string
        print(f"${value}$")


command_entry, value_entry = input(), input()
if value_entry.isnumeric():
    value_entry = int(value_entry)

data_types(command_entry, value_entry)
# print(type(data_types(command_entry, value_entry)))



