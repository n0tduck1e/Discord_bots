#!/usr/bin/env python

import discord
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

import pkg.vt.vt

class dr_plague:
	def __init__(self):
		self.insults = cache_insults()

def init_bot():
	global bot, bot_token, instance_list
	bot_token = os.environ["DISCORD_TOKEN"]

	intents = discord.Intents.default()
	intents.typing = True
	intents.presences = True
	intents.message_content = True
	intents.guild_messages = True

	bot = commands.Bot(intents=intents,command_prefix='!')
	bot.remove_command('help')

def run_bot():
	bot.run(bot_token)

def message_lister():
	global bot

	@bot.event
	async def on_ready():
		print("Bot is ready to be used\n")
		async for guild in bot.fetch_guilds(limit=150):
			print(f"Guild Name: {guild.name} / Guild ID: {guild.id}")

	@bot.event
	async def on_guild_join(guild):
		print('Bot has been added to a new server')

	@bot.event
	async def on_message(message):
		if message.author == bot.user:
			pass
		elif "69" in message.content:
			await message.channel.send('Nice')
		key_words = {'hard','long'}
		for i in key_words:
			if i in message.content:
				await message.channel.send('thats what she said')
				break
		await bot.process_commands(message)

def command_working():
	global bot
	@bot.command(name="help")
	async def help(ctx):
		if ctx.author == 'Vatsal':
			ctx.send('No help for you, weeb')
		else:
			await ctx.send('''
Basic Bot:
!help => help
!vtsearch => search vt query (limit is 5 to avoid noise)
!vtdownload => download samples from single or a list of hashes (space separated)
''')

	@bot.command(name="vtdownload")
	@has_permissions(attach_files = True)
	async def vtdownload(ctx,*hashlist):
		if len(hashlist) == 0:
			await ctx.send("no hash provided")
		await pkg.vt.vt.download_files(ctx,hashlist)

	@bot.command(name="vtsearch")
	@has_permissions(attach_files = True)
	async def vtsearch(ctx,search):
		await pkg.vt.vt.get_results(ctx,search)

	@bot.command(name="clear")
	@has_permissions(manage_messages=True)
	async def clear(ctx,amount=20):
		await ctx.channel.purge(limit=amount)

	@bot.command(name="kick")
	@has_permissions(kick_members=True)
	async def _kick(ctx,member: discord.Member, *, reason=None):
		await member.kick(reason=reason)

	@bot.command(name="ban")
	@has_permissions(ban_members=True)
	async def _ban(ctx,member: discord.Member, *, reason=None):
		await member.ban(reason=reason)

	@bot.command(name="unban")
	@has_permissions(ban_members=True)
	async def _unban(ctx, *, member):
		a = await ctx.guild.bans()
		name, number = str(member).split('#')
		for i in a:
			if (name,number) == (i.user.name, i.user.discriminator):
				await ctx.guild.unban(i.user)
				await ctx.send(f'The user @{i.user.mention} has been unbanned.')    

def main():
	init_bot()
	message_lister()
	command_working()
	run_bot()

if __name__ == "__main__":
	main()
