from url import Url
from random import shuffle

class Tournament():
    def __init__(self):
        self.filename = 'participantes.txt'

    def register_participant(self, participant):
        with open(self.filename, "a") as f:
            f.write(f'{participant}\n')

    def clear_file(self):
        open(self.filename, 'w').close()

    def create_bracket(self):
        url = Url()
        with open(self.filename, 'r') as f:
            persons = []
            for participant in f.readlines():
                persons.append(participant)
            shuffle(persons)
            [url.add(person) for person in persons]
        return url.show()
