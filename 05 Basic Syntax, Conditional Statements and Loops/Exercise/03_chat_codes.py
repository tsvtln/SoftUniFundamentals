n = int(input())
for messages in range(n):
    message_code = int(input())
    if message_code == 88:
        print('Hello')
    elif message_code == 86:
        print('How are you?')
    elif message_code != 88 and message_code != 86 and message_code < 88:
        print('GREAT!')
    elif message_code > 88:
        print('Bye.')
