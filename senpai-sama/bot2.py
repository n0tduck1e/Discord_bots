#!/usr/bin/env python

import discord
import requests
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
from bs4 import BeautifulSoup

bot = discord.Client()
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


'''making get request so doesnt have make everytime '''


r = requests.get('https://thoughtcatalog.com/lorenzo-jensen-iii/2016/11/sick-burns-the-100-greatest-insults-of-all-time/')
soup = BeautifulSoup(r.text,'lxml')
a = soup.find('div',{'class':'entry post clearfix'}).find_all('p')



def message_lister():
    @bot.event
    async def on_ready():
        print("Bot is ready to be used\n")

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

    @bot.command(name="help")
    async def help(ctx):
        if ctx.author == 'Vatsal':
            ctx.send('No help for you, weeb')
        else:
            await ctx.send("help")

    @bot.command()
    async def clear(ctx,amount=20):
            if "duckie#8881" in str(ctx.message.author):
                await ctx.channel.purge(limit=amount)
    
            else:
                id = "<@509382450841911307>"
                await ctx.send("Wait a minute, you aint {}".format(id))

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



    
    
    @bot.command()
    async def insult(ctx):
        c = random.randint(0,100)
        await ctx.send(a[c].text)
    bot.run('NjI4MjQxNTcwNzkzMTI3OTU3.XaCV_A.3F7LmzHaoZ8ZITPFZCEm6Kw9gyg')

message_lister()
command_working()

