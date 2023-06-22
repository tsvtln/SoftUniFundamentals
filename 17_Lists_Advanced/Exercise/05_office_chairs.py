rooms = int(input())
fc = 0
NEC = False
for room in range(1, rooms + 1):
    chairs_visitors = input().split()
    chairs = int(len(chairs_visitors[0]))
    visitors = int(chairs_visitors[1])
    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room}")
        NEC = True
    else:
        fc += chairs - visitors

if not NEC:
    print(f"Game On, {fc} free chairs left")
