class Party:
    def __init__(self):
        self.people = []

    @staticmethod
    def receiver():
        command = ''
        party = Party()
        while command != 'End':
            command = input()
            if command == 'End':
                continue
            party.people.append(command)
        return f"Going: {', '.join(party.people)}", f"Total: {len(party.people)}"

    @staticmethod
    def output():
        party = Party()
        going, total = party.receiver()
        print(going + "\n" + total)


Party.output()
