#!/usr/bin/env python
"""Bot class"""
import os
from twitchio.ext import commands
from tournament import Tournament

class Bot(commands.Bot):
    """map the commands of twitch"""
    def __init__(self):
        self.tournament = Tournament()
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
            self.tournament.register_participant(name_participant[:20])
            await context.send(f'{name_participant} se anoto en el torneo. Participante N°{Tournament.persons}')
        except Exception as error:
            print(error)

    @commands.command(name='clear')
    async def clear(self, context):
        """this method clear all the participants"""
        try:
            if context.author.is_mod:
                self.tournament.clear_file()
                await context.send('vaciando la lista...')
        except Exception as error:
            print(error)

    @commands.command(name='stop')
    async def stop(self, context):
        """this method show the finally url of the tournament"""
        try:
            if context.author.is_mod:
                self.tournament.start = False
                bracket_url = self.tournament.create_bracket()
                print(bracket_url)
                await context.send(bracket_url)
        except Exception as error:
            print(error)

    @commands.command(name='start')
    async def start(self, context):
        """this method start the bot"""
        try:    
            if context.author.is_mod:
                self.tournament.start = True
                self.tournament.clear_file()
                await context.send('Arrancando el torneo manda !yo y tu nombre')
        except Exception as error:
            print(error)

    @commands.command(name='remove')
    async def remove(self, context):
        """remove one person to tournament"""
        try:    
            if context.author.is_mod:
                name_to_remove = self.get_params_as_text(context)
                self.tournament.remove(name_to_remove)
        except Exception as error:
            print(error)

    @commands.command(name='tabla')
    async def remove(self, context):
        """remove one person to tournament"""
        try:    
            url_tournament = Tournament.last_url_tournament
            await context.send(url_tournament)
        except Exception as error:
            print(error)


    @commands.command(name='info')
    async def info(self, context):
        """this method show info of the bot"""
        await context.send('creador: debellisnahuel@gmail.com')

# TODO reporte de wins
# TODO mostrar tabla actualizada y que no la genere de nuevo
# TODO ver que poronga pasaba con el link en otros browsers
