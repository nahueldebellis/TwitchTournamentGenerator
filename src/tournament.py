#!/usr/bin/env python
"""Tournament class"""
from random import shuffle
from url import Url

class Tournament():
    """this class randomize the participats, and add participants to a file"""
    def __init__(self):
        self.filename = 'participantes.txt'
        self.start = False

    def register_participant(self, participant):
        """insert in file a new participant"""
        if self.start:
            with open(self.filename, "a") as file_participants:
                file_participants.write(f'{participant}\n')
        else:
            raise Exception('no init the tournament')

    def clear_file(self):
        """clear file of participants"""
        if self.start:
            open(self.filename, 'w').close()

    def create_bracket(self):
        """create brackets and return the url string"""
        if not self.start:
            url = Url()
            with open(self.filename, 'r') as file_participants:
                persons = file_participants.readlines()
                shuffle(persons)
                for person in persons:
                    url.add(person)
            return url.show()
        raise Exception('no init the tournament')
