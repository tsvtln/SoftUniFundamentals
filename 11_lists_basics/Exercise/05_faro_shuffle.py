cards = input().split(' ')
shuffles = int(input())
for shuffle in range(shuffles):
    sorted_cards = []
    middle_of_the_deck = len(cards) // 2
    left_part = cards[:middle_of_the_deck]
    right_part = cards[middle_of_the_deck:]
    for card in range(len(left_part)):
        sorted_cards.append(left_part[card])
        sorted_cards.append(right_part[card])
    cards = sorted_cards
print(sorted_cards)
