import os
import re
from discord.ext import commands
from discord import FFmpegPCMAudio
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
	print(f'{client.user.name} is connected to Discord!')

@client.event
async def on_member_join(member):
	await member.create_dm()
	await member.dm_channel.send(f'WAAAAAAAAAAAAAAAAAAAAAAAAASUUUUUP {member.name.mention}!')

@client.command(name='duck', help="Gives you a duckduckgo link for the given search values! Usage: .duck <searchValue 1>-<searchValue 2> ...")
async def duck_link(ctx, *, message):
	if len(message) < 1:
		await ctx.send('Invalid arguments! Usage: .duck <searchValue 1> <searchValue 2> ...')
		return
	
	parts = ""
	for part in message:
		parts += part
	
	parts = re.sub(r"\s", '_', parts)
	

	link = 'https://www.duckduckgo.com/' + parts
	await ctx.send(f"{ctx.message.author.mention} Here is your requested link: " + link)

@client.command(name='quit', help="If you think i can be quitted, you're wrong!")
async def quit_bot(ctx):
	

	if "mexam" in ctx.message.author.name:
		await ctx.send(f"I shall not be quitted! Ach ja, und {ctx.message.author.mention} ist cool ;)")
	else:
		await ctx.send(f"I shall not be quitted! Ach ja, und {ctx.message.author.mention} ist ein Noob ;)")

@client.command(name='join', help="Joins the voice channel you're currently in")
async def join_voice(ctx):
	try:
		channel = ctx.author.voice.channel
		await channel.connect()
		await ctx.send("Sucessfully joined your voice channel")
	except Exception as e:
		print(e)
		await ctx.send(f"ERROR: You're not in a voice channel {ctx.message.author.mention}")

@client.command(name='exit-channel', help="Leaves the voice channel")
async def exit_voice(ctx):
	try:
		await ctx.voice_client.disconnect()
		await ctx.send("Sucessfully left the voice channel")
	except Exception as e:
		print(e)
		await ctx.send(f"ERROR: {ctx.message.author.mention} You stupid? I'm not in a voice channel!")

@client.command(name='payai', help="Plays Ich hab garnichts gemacht")
async def play_payai(ctx):
	try:
		channel = ctx.author.voice.channel
		vc = await channel.connect()
		audio = FFmpegPCMAudio('garnichts.mp3')
		if not vc.is_playing():
			await ctx.send("PAAAAAAAAAAAYAAAAAAAAAAAI, ICH HAB GANIX GEMAKT")
			vc.play(audio, after=None)
	except Exception as e:
		print(e)
		await ctx.send(f"Something went wrong playing the song...")

		
@client.command(name='stop', help="Stops playing music")
async def stop_music(ctx):
	ctx.voice_client.stop()

client.run(TOKEN)
