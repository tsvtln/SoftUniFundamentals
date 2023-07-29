import re

receive_mails = input()
filter_mails = r"\s(?P<name>[a-z0-9]+[a-z0-9\.\-\_]*)@(?P<domain>[a-z0-9]+[a-z0-9\.\-\_]*)(?P<site>\.[a-z]+)\b"

# get_mail_address = re.findall(filter_mails, receive_mails)
get_mail_address = re.finditer(filter_mails, receive_mails)
for match in get_mail_address:
    name = match.group("name")
    domain = match.group("domain")
    site = match.group("site")
    email_address = f"{name}@{domain}{site}"
    print(email_address)
