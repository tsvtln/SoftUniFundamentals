import re
phone = input()
regex = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"

valid_phones = re.findall(regex, phone)

print(", ".join(valid_phones))