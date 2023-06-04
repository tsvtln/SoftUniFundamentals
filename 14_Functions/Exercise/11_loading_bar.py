def loading_bar(bar_level):
    if bar_level == 100:
        return f'100% Complete!\n[%%%%%%%%%%]'
    else:
        return f"{bar_level}% [{'%' * (bar_level // 10)}" \
               f"{'.' * (10 - (bar_level // 10))}]" \
               f"\nStill loading..."


entry = int(input())
print(loading_bar(entry))
