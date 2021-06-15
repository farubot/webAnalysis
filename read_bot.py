import discord
from discord.ext import commands
import subprocess
import ffmpeg
from voice_generator import creat_WAV

client = commands.Bot(command_prefix='.')
voice_client = None


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command()
async def join(ctx):
    # voicechannelを取得
    vc = ctx.author.voice.channel
    # voicechannelに接続
    await vc.connect()


@client.command()
async def bye(ctx):
    # 切断
    await ctx.voice_client.disconnect()


@client.event
async def on_message(message):
    msgclient = message.guild.voice_client
    if message.content.startswith('.'):
        pass

    else:
        if message.guild.voice_client:
            print(message.content)
            creat_WAV(message.content)
            source = discord.FFmpegPCMAudio("output.wav")
            message.guild.voice_client.play(source)
        else:
            pass
    await client.process_commands(message)

client.run("ODUyNDUyNTgxNDY3ODgxNDcy.YMHCVQ.eXhr3YLaZlak9EhP6zTMXg8ZM00")
