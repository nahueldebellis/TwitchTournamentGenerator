import os
from twitchio.ext import commands
from tournament import Tournament

class Bot(commands.Bot):
    def __init__(self):
        self.annotate = Tournament()
        super().__init__(irc_token = os.environ['TOKEN'], client_id=os.environ['CLIENT_ID'],
                         nick=os.environ['BOT_NICK'], prefix="!", initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        print(f'Ready | {self.nick}')

    @commands.command(name='join')
    async def join(self, context):
        command, *name_participant = context.message.content.split(' ')
        name_participant = ' '.join(name_participant)
        self.annotate.register_participant(name_participant)

    @commands.command(name='clear')
    async def clear(self, context):
        self.annotate.clear_file()

    @commands.command(name='start')
    async def clear(self, context):
        pass
    
    @commands.command(name='stop')
    async def clear(self, context):
        pass
    
    @commands.command(name='info')
    async def info(self, context):
        await context.send('creador: debellisnahuel@gmail.com')
        
if __name__ ==  "__main__":
    bot = Bot()
    bot.run()
        
        
    
