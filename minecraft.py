import discord
import subprocess
import paramiko
import time

# Enter your access token
TOKEN = 'enter your access token'
# Enter the path to start.sh
STARTSH = 'Enter the path to start.sh'
# Enter the path to stop.sh
STOPSH = 'Enter the path to start.sh'

client = discord.Client()


@client.event
async def on_ready():
    # Processes running at startup
    print('ログインしました。')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    if message.content == '/start m':
        subprocess.run([STARTSH, 'arguments'], shell=True)
        await message.channel.send('開始スクリプトを実行しました。')
        await message.channel.send('task ok')
    if message.content == '/stop m':
        subprocess.run([STOPSH, 'arguments'], shell=True)
        await message.channel.send('task ok')
        await message.channel.send('停止スクリプトを実行しました。完全に停止するまで1分ほどお待ちください。')


client.run(TOKEN)
