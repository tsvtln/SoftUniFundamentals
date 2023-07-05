from turtle import position

possible_items = {
    "Shadowmourne": 250,  # shards
    "Valanyr": 250,  # fragments
    "Dragonwrath": 250  # motes
}
collected_materials = {}
collect = input().lower().split()
shards, fragments, motes = 0, 0, 0
for k in range(0, len(collect), 2):
    if collect[k + 1] not in collected_materials:
        collected_materials[collect[k + 1]] = int(collect[k])
    else:
        collected_materials[collect[k + 1]] += int(collect[k])


for material, amount in collected_materials.items():
    amount = int(amount)
    if material == 'shards':
        shards += amount
        if shards >= possible_items.get("Shadowmourne"):
            shards -= 250
            collected_materials["shards"] = shards
            print("Shadowmourne obtained!")
            break
    elif material == 'fragments':
        fragments += amount
        if fragments >= possible_items.get("Valanyr"):
            fragments -= 250
            collected_materials["fragments"] = fragments
            print("Valanyr obtained!")
            break
    elif material == 'motes':
        motes += amount
        if motes >= possible_items.get("Dragonwrath"):
            motes -= 250
            collected_materials["motes"] = motes
            print("Dragonwrath obtained!")
            break

for left_material, left_amount in collected_materials.items():
    print(f"{left_material}: {left_amount}")

