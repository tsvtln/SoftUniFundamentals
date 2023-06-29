class Email:
    def __init__(self, sender, receiver, content):
        self.sender, self.receiver, self.content, self.is_sent = sender, receiver, content, False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

    @staticmethod
    def get_mail() -> list:
        command, mails = '', []
        while command != 'Stop':
            command = input()
            if command == 'Stop':
                continue
            sender, receiver, content = command.split()
            email = Email(sender, receiver, content)
            mails.append(email)
        indexes = [int(x) for x in input().split(', ')]
        [mails[sent].send() for sent in indexes]
        [print(mail.get_info()) for mail in mails]


Email.get_mail()
