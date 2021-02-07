#!/usr/bin/env python
"""Url class"""
class Url():
    """This class format participants and add to an url"""
    cant_participants = 0
    bracket = 0
    def __init__(self):
        self.url_final = ['https://scorecounter.com/tournament/?set=', '31001111000000']
        self.concat = '&'
        self.treintaydos = '5'
        self.dieciseis = '4'
    def add(self, participant):
        """add new pasticipant to the bracket"""
        Url.bracket = Url.bracket if Url.cant_participants % 2 else Url.bracket+1
        Url.cant_participants = Url.cant_participants+1
        position = 'home' if Url.cant_participants % 2 else 'visitor'
        self.url_final.append(f'{self.concat}{position}1-{Url.bracket}={participant}')
    def show(self):
        """concat the url and return the string"""
        if Url.cant_participants <= 32:
            self.url_final[1] = self.treintaydos+self.url_final[1][1:]
        if Url.cant_participants <= 16:
            self.url_final[1] = self.dieciseis+self.url_final[1][1:]
        Url.cant_participants = 0
        Url.bracket = 0
        return ''.join(self.url_final)
