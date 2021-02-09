#!/usr/bin/env python
"""Tournament class"""
from random import shuffle
from url import Url

class Tournament():
    """this class randomize the participats, and add participants to a file"""
    persons = 1
    last_url_tournament = "No se genero aun el torneo"
    def __init__(self):
        self.filename = 'participantes.txt'
        self.participants = []
        self.start = False

    def register_participant(self, participant):
        """insert in file a new participant"""
        if self.start:
            Tournament.persons = Tournament.persons + 1
            self.participants.append(participant)
        else:
            raise Exception('no init the tournament')

    def clear_file(self):
        """clear file of participants"""
        if self.start:
            self.participants = []

    def create_bracket(self):
        """create brackets and return the url string"""
        if not self.start:
            url = Url()
            shuffle(self.participants)
            if len(self.participants) > 32:
                self.participants = self.participants[:32]
            for participant in self.participants:
                url.add(participant)
            Tournament.last_url_tournament = url.show()
            return Tournament.last_url_tournament
        raise Exception('no init the tournament')

    def remove(self):
        """remove one name in the list"""
        pass
