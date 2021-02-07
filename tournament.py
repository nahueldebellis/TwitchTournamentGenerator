

class Tournament():
    def __init__(self):
        self.filename = 'participantes.txt'

    def register_participant(self, participant):
        with open(self.filename, "a") as f:
            f.write(f'{participant}\n')

    def clear_file(self):
        open(self.filename, 'w').close()

    def create_bracket():
        url = Url()
        home, visitor = 
        with open(self.filename, 'r') as f:
            participant = f.read()
            url.add(participant)
        return ''


home1-1=nhdb&visitor1-1=adsf&home1-2=juanito&visitor1-2=emi&home1-3=garza&visitor1-3=sarasa&home1-4=%5Batata&visitor1-4=saba
