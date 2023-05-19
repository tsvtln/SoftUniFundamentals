num_of_lines = int(input())
BALANCED, RECEIVED_BRACKET, FIRST_CLOSER, OPEN, CLOSE = False, False, False, False, False

for _ in range(num_of_lines):
    recieve = input()
    if recieve == '(' or recieve == ')' and not RECEIVED_BRACKET:
        RECEIVED_BRACKET = True
        if recieve == ')':
            FIRST_CLOSER = True
    if OPEN and not CLOSE and recieve == '(':
        FIRST_CLOSER = True
    if recieve == '(' and RECEIVED_BRACKET:
        OPEN = True
        BALANCED = False
    elif recieve == ')' and OPEN and RECEIVED_BRACKET:
        CLOSE = True
        BALANCED = True
    if OPEN and CLOSE and RECEIVED_BRACKET:
        OPEN = False
        CLOSE = False
    if recieve == '((':
        FIRST_CLOSER = True

if FIRST_CLOSER or not BALANCED:
    print('UNBALANCED')
else:
    print('BALANCED')
