cant_participants = 0
bracket = 0
class Url():

    def __init__(self):
        self.url_final = ['https://scorecounter.com/tournament/?set=31001111000000']
        self.concat = '&'
        self.treintaydos = 5
        self.dieciseis = 4
        self.ocho = 3

    def add(self, participant):
        global cant_participants, bracket
        bracket = bracket if cant_participants % 2 else bracket+1
        cant_participants = cant_participants+1
        position =  'home' if cant_participants % 2 else 'visitor'
        self.url_final.append(f'{self.concat}{position}1-{bracket}={participant}')
    
    def show(self):
        global cant_participants, bracket
        cant_participants = 0
        bracket = 0
        return ''.join(self.url_final)

