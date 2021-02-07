from url import Url
from random import shuffle

class Tournament():
    def __init__(self):
        self.filename = 'participantes.txt'
        self.start = False

    def register_participant(self, participant):
        if self.start:
            with open(self.filename, "a") as f:
                f.write(f'{participant}\n')
        else:
            raise Exception('no init the tournament')

    def clear_file(self):
        if self.start:
            open(self.filename, 'w').close()

    def create_bracket(self):
        if not self.start:
            url = Url()
            with open(self.filename, 'r') as f:
                persons = []
                for participant in f.readlines():
                    persons.append(participant)
                shuffle(persons)
                [url.add(person) for person in persons]
            return url.show()
