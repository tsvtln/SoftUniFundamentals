name_phone = '---'
phone_book = dict()
while len(name_phone) > 2:
    name_phone = input()
    if len(name_phone) < 2:
        continue
    name, phone = name_phone.split('-')
    # for data in name_phone:
    phone_book[name] = phone

search = int(name_phone)
for lookup in range(search):
    search_contact = input()
    if search_contact in phone_book:
        print(f"{search_contact} -> {phone_book.get(search_contact)}")
    else:
        print(f"Contact {search_contact} does not exist.")
