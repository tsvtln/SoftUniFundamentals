import re

pattern = r"(www\.([A-Za-z0-9\-]+)\.[a-z]+(\.[a-z]+)*)"


string = input()
while string:
    mails = re.search(pattern, string)
    if mails:
        print(mails.group(0))

    string = input()



