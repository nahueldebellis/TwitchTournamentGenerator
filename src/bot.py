#!/usr/bin/env python
"""Bot class"""
import os
from twitchio.ext import commands
import requests

class Bot(commands.Bot):
    """map the commands of twitch"""
    def __init__(self):
        self.participants = list()
        self.begining = False
        self.url = 'http://192.168.1.67:8080'
        super().__init__(irc_token = os.environ['TOKEN'], client_id=os.environ['CLIENT_ID'],
                         nick=os.environ['BOT_NICK'], prefix="!",
                         initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        """starting method"""
        print(f'Ready | {self.nick}')

    def get_params_as_text(self, context):
        """get a string with all the text after the command"""
        try:
            command, *params = context.message.content.split(' ')
            params = ' '.join(params)
            return params
        except Exception as error:
            print(error)

    @commands.command(name='yo')
    async def join(self, context):
        """this method add a nex participant"""
        try:
            name_participant = self.get_params_as_text(context)

            self.participants.append(name_participant)

            await context.send(f'{name_participant} se anoto en el torneo. Participante N°')
        except Exception as error:
            print(error)

    @commands.command(name='clear')
    async def clear(self, context):
        """this method clear all the participants"""
        try:
            if context.author.is_mod:
                self.participants.clear()
                await context.send('vaciando la lista...')
        except Exception as error:
            print(error)

    @commands.command(name='stop')
    async def stop(self, context):
        """this method show the finally url of the tournament"""
        try:
            if context.author.is_mod:
                self.begining = False
                requests.post(f'{self.url}/test', json = { 'participants': self.participants })
                await context.send('guardado')
        except Exception as error:
            print(error)

    @commands.command(name='start')
    async def start(self, context):
        """this method start the bot"""
        try:    
            if context.author.is_mod:
                self.begining = True
                await context.send('Arrancando el torneo manda !yo y tu nombre')
        except Exception as error:
            print(error)

    @commands.command(name='tabla')
    async def remove(self, context):
        """remove one person to tournament"""
        try:    
            url_table_tournament = requests.get(f'{self.url}/tabla')
            await context.send(url_table_tournament)
        except Exception as error:
            print(error)


    @commands.command(name='info')
    async def info(self, context):
        """this method show info of the bot"""
        await context.send('creador: debellisnahuel@gmail.com')

# TODO reporte de wins
# TODO mostrar tabla actualizada y que no la genere de nuevo
# TODO ver que poronga pasaba con el link en otros browsers
