first, second = input(), input()
while first in second:
    second = second.replace(first, "")
print(second)