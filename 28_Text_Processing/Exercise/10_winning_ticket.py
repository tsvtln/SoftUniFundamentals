def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"
    winning_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbols_repetition = match_symbol * uninterrupted_match_length
            if winning_symbols_repetition in left_part and winning_symbols_repetition in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(check_ticket(ticket))


"""100/100"""
# tickets = input().split(', ')
# count_win = ''
# last_char = ''
# winning_chars = ["$", "@", "#", "^"]
# # win_char = ''
# FH = False
# WIN = False
# JACKPOT = False
# JACKPOT_WON = False
# for ticket in tickets:
#     ticket = ticket.strip()
#     if len(ticket) != 20:
#         print(f"invalid ticket")
#         continue
#     count_win = ''
#     last_char = ''
#     FH = False
#     WIN = False
#     JACKPOT = False
#     JACKPOT_WON = False
#     for char in ticket[10:]:
#         if char in winning_chars:
#             if last_char != char:
#                 last_char = char
#                 count_win = char
#                 # win_char = char
#             elif last_char == char:
#                 count_win += char
#         elif char not in winning_chars:
#             if len(count_win) >= 6 and not FH:
#                 FH = True
#             elif len(count_win) >= 6 and FH:
#                 WIN = True
#                 break
#         if len(count_win) == 10 or len(count_win) // 2 == 10:
#             if not JACKPOT:
#                 JACKPOT = True
#             elif JACKPOT:
#                 JACKPOT_WON = True
#                 break
#     last_char = ''
#     for char in ticket[:10]:
#         if char in winning_chars:
#             if last_char != char:
#                 last_char = char
#                 count_win = char
#                 # win_char = char
#             elif last_char == char:
#                 count_win += char
#         elif char not in winning_chars:
#             if len(count_win) >= 6 and not FH:
#                 FH = True
#             elif len(count_win) >= 6 and FH:
#                 WIN = True
#                 break
#         if len(count_win) == 10 or len(count_win) // 2 == 10:
#             if not JACKPOT:
#                 JACKPOT = True
#             elif JACKPOT:
#                 JACKPOT_WON = True
#                 break
#     if WIN:
#         # win_char = set(count_win)
#         print(f'ticket "{ticket}" - 6{count_win[0]}')
#     elif JACKPOT_WON:
#         # win_char = set(count_win)
#         print(f'ticket "{ticket}" - 10{count_win[0]} Jackpot!')
#     else:
#         print(f'ticket "{ticket}" - no match')
