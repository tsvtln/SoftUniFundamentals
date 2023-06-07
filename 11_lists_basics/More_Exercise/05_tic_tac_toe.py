line_one = [int(line_one) for line_one in input().split()]
line_two = [int(line_two) for line_two in input().split()]
line_three = [int(line_two) for line_two in input().split()]
FP_WIN, SP_WIN = False, False

# Check first player win conditions
if line_one[0] == 1 and line_two[1] == 1 and line_three[2] == 1 or \
        line_one[2] == 1 and line_two[1] == 1 and line_three[0] == 1 or \
        line_one[0] == 1 and line_two[0] == 1 and line_three[0] == 1 or \
        line_one[1] == 1 and line_two[1] == 1 and line_three[1] == 1 or \
        line_one[2] == 1 and line_two[2] == 1 and line_three[2] == 1 or \
        line_one[0] == 1 and line_one[0] == 1 and line_one[0] == 1 or \
        line_two[0] == 1 and line_two[1] == 1 and line_two[2] == 1 or \
        line_three[0] == 1 and line_three[1] == 1 and line_three[2] == 1:
    FP_WIN = True

# Check second player win conditions
if line_one[0] == 2 and line_two[1] == 2 and line_three[2] == 2 or \
        line_one[2] == 2 and line_two[1] == 2 and line_three[0] == 2 or \
        line_one[0] == 2 and line_two[0] == 2 and line_three[0] == 2 or \
        line_one[1] == 2 and line_two[1] == 2 and line_three[1] == 2 or \
        line_one[2] == 2 and line_two[2] == 2 and line_three[2] == 2 or \
        line_one[0] == 2 and line_one[0] == 2 and line_one[0] == 2 or \
        line_two[0] == 2 and line_two[1] == 2 and line_two[2] == 2 or \
        line_three[0] == 2 and line_three[1] == 2 and line_three[2] == 2:
    SP_WIN = True

if FP_WIN:
    print("First player won")
elif SP_WIN:
    print("Second player won")
else:
    print("Draw!")
