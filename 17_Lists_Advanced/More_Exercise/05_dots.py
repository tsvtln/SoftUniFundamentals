def correct_lab_bounds(row, col):
    if row < 0 or col < 0 or row >= len(lb) or col >= len(lb[0]):
        return True


def check_wall(row, col):
    if lb[row][col] in "-–":
        return True


def check_already_visit(row, col):
    if lb[row][col] == "v":
        return True


def find_exit(row, col):
    if lb[row][col] == ".":
        return True


def find_the_lab_path(row, col, lab):
    if correct_lab_bounds(row, col) or check_wall(row, col) or check_already_visit(row, col):
        return
    path_steps.append(1)
    if find_exit(row, col):
        max_connected_points.append(sum(path_steps))
    lab[row][col] = "v"
    find_the_lab_path(row, col + 1, lab)
    find_the_lab_path(row, col - 1, lab)
    find_the_lab_path(row + 1, col, lab)
    find_the_lab_path(row - 1, col, lab)


row_entry = int(input())
lb = []
max_connected_points = [0]
for curr_row in range(row_entry):
    lb.append(list(input().split()))
range_of_col = len(lb[0])
for row_entry in range(len(lb)):
    for clmn in range(range_of_col):
        path_steps = []
        if not check_wall(row_entry, clmn):
            find_the_lab_path(row_entry, clmn, lb)
print(max(max_connected_points))
