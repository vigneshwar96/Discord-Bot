import discord
import requests
import json
def get_meme():
    response=requests.get('https://meme-api.com/gimme')
    json_data=json.loads(response.text)
    return json_data['url']  
class Myclient (discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
      if message.author == self.user:
        return
      if message.content.startswith('$meme'):
        await message.channel.send(get_meme())
intents = discord.Intents.default()
intents.message_content=True
client=Myclient(intents=intents)
client.run('MTQ1MDk5NTE2ODc4MTAwODk3Nw.GM0ovd.SkMm2mx6-7ueST9AjRi1sOIuK2xmolF1AM-jYA')
 
        
     
