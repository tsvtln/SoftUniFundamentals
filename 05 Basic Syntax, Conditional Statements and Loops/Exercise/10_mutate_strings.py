s1, s2 = input(), input()
cs = s1
for i in range(len(s1)):
    ptw = s2[:i + 1] + s1[i + 1:]
    if ptw == cs:
        continue
    else:
        cs = ptw
        print(ptw)
