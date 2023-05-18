qt, days_tc, days, total_cost, spirit, ELV = int(input()), int(input()), 0, 0, 0, False
prc_ornament, prc_tree_skirt, prc_tree_garland, prc_tree_lights = 2, 5, 3, 15
pts_ornament, pts_tree_skirt, pts_tree_garland, pts_tree_lights = 5, 3, 10, 17

for days in range(1, days_tc + 1):
    if days % 11 == 0:
        qt += 2
    if days % 2 == 0:
        total_cost += prc_ornament * qt
        spirit += pts_ornament
    if days % 3 == 0:
        total_cost += prc_tree_skirt * qt
        total_cost += prc_tree_garland * qt
        spirit += pts_tree_skirt + pts_tree_garland
    if days % 5 == 0:
        total_cost += prc_tree_lights * qt
        spirit += pts_tree_lights
    if days % 3 == 0 and days % 5 == 0:
        spirit += 30
    if days % 10 == 0:
        spirit -= 20
        total_cost += prc_tree_skirt + prc_tree_garland + prc_tree_lights
if days_tc % 10 == 0:
    spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
