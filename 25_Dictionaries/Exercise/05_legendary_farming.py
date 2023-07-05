items = {"shards": 0, "fragments": 0, "motes": 0}
current_items = input().split()
obtained = False
while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in items.keys():
            items[key] = 0
        items[key] += value
        if items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            items["shards"] -= 250
            obtained = True
        elif items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            items["fragments"] -= 250
            obtained = True
        elif items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            items["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break
    current_items = input().split()
for material, quantity in items.items():
    print(f"{material}: {quantity}")
# possible_items = {
#     "Shadowmourne": 250,  # shards
#     "Valanyr": 250,  # fragments
#     "Dragonwrath": 250  # motes
# }
# collected_materials = {}
# final_materials = {}
# collect = input().lower().split()
# FOUND = False
# shards, fragments, motes = 0, 0, 0
#
# while not FOUND:
#
#     for k in range(0, len(collect), 2):
#         if collect[k + 1] not in collected_materials:
#             collected_materials[collect[k + 1]] = int(collect[k])
#         else:
#             collected_materials[collect[k + 1]] += int(collect[k])
#         if 'motes' in collected_materials and collected_materials['motes'] >= 250 or 'shards' in collected_materials and \
#                 collected_materials['shards'] >= 250 or 'fragments' in collected_materials and \
#                 collected_materials['fragments'] >= 250:
#             break
#
#     for material, amount in collected_materials.items():
#         amount = int(amount)
#         if material == 'shards' and not FOUND:
#             shards += amount
#             if shards >= possible_items.get("Shadowmourne"):
#                 shards -= 250
#                 final_materials["shards"] = shards
#                 print("Shadowmourne obtained!")
#                 FOUND = True
#         elif material == 'fragments' and not FOUND:
#             fragments += amount
#             if fragments >= possible_items.get("Valanyr"):
#                 fragments -= 250
#                 final_materials["fragments"] = fragments
#                 print("Valanyr obtained!")
#                 FOUND = True
#         elif material == 'motes' and not FOUND:
#             motes += amount
#             if motes >= possible_items.get("Dragonwrath"):
#                 motes -= 250
#                 final_materials["motes"] = motes
#                 print("Dragonwrath obtained!")
#                 FOUND = True
#         if material not in final_materials and not FOUND:
#             final_materials[material] = amount
#         elif material in final_materials and not FOUND:
#             final_materials[material] += amount
#     if not FOUND:
#         collected_materials.clear()
#         collect = input().lower().split()
#
# if 'shards' in final_materials:
#     shards = collected_materials.get('shards')
#     del final_materials['shards']
# if 'fragments' in final_materials:
#     fragments = collected_materials.get('fragments')
#     del final_materials['fragments']
# if 'motes' in final_materials:
#     motes = collected_materials.get('motes')
#     del final_materials['motes']
#
# print(f"shards: {shards}\nfragments: {fragments}\nmotes: {motes}")
#
# for left_material, left_amount in final_materials.items():
#     print(f"{left_material}: {left_amount}")
