#!/usr/bin/env python
"""Bot class"""
import os
from twitchio.ext import commands
from tournament import Tournament

class Bot(commands.Bot):
    """map the commands of twitch"""
    def __init__(self):
        self.annotate = Tournament()
        super().__init__(irc_token = os.environ['TOKEN'], client_id=os.environ['CLIENT_ID'],
                         nick=os.environ['BOT_NICK'], prefix="!",
                         initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        """starting method"""
        print(f'Ready | {self.nick}')

    @commands.command(name='join')
    async def join(self, context):
        """this method add a nex participant"""
        command, *name_participant = context.message.content.split(' ')
        name_participant = ' '.join(name_participant)
        self.annotate.register_participant(name_participant)

    @commands.command(name='clear')
    async def clear(self, context):
        """this method clear all the participants"""
        self.annotate.clear_file()
        await context.send('vaciando la lista...')

    @commands.command(name='stop')
    async def stop(self, context):
        """this method show the finally url of the tournament"""
        self.annotate.start = False
        bracket_url = self.annotate.create_bracket()
        await context.send(bracket_url)

    @commands.command(name='start')
    async def start(self, context):
        """this method start the bot"""
        self.annotate.start = True
        await context.send('Arrancando el torneo manda !join y tu nombre')

    @commands.command(name='info')
    async def info(self, context):
        """this method show info of the bot"""
        await context.send('AL QUE PONE UN CARACTER RARO LO FUNAMOS \n \
            creador: debellisnahuel@gmail.com')

if __name__ ==  "__main__":
    bot = Bot()
    bot.run()
