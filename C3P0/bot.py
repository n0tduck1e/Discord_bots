#!/usr/bin/env python

import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

#All this so key doesnt leak through source code, dm me if you it
#fuk of hackers
f = open('secret.key','rt')
TOKEN = f.readline().strip('\n')

print(TOKEN)

client = commands.Bot(command_prefix='!')
client.remove_command('help')

def event_working():
    @client.event
    async def on_ready():
        print("Bot logged in as {}".format(client.user))
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        if "69" in message.content:
            await message.channel.send('Nice')
        await client.process_commands(message)
    @client.event
    async def on_member_join(member : discord.Member):
        for i in member.guild.channels:
            if str(i) == "welcome":
                await i.send('Welcome to **PwnBpit**, {}.\n Type !help to use the bot.'.format(member.mention))
    
    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No Luke, You Must First Become A Jedi")
        else:
            text = '''
Invalid Command. Read !help for more info
'''
            await ctx.send(text)


    
def command_working():
    
    @client.command()
    async def help(ctx):
        text =  '''
```
The help has arrived !!

               |||      |||
               | |  __  | |
|-|_____-----/   |_|  |_|   \\-----_____|-|
|_|_________{   }|  (^) |{  }__________|_|
 ||          |_| |   ^  | |_|          ||
 |              \\|  /\\  |/              |
 |               \\ |--| /               |
 =               \\ |__| /               =
 +               \\      /               +
                  \\    /
                  \\    /
                   \\  /
                   \\  /
                   \\  /
                   \\  /
                   \\  /
                   \\  /
                    \\/


Commnad prefix is  !
Type the following commands to get stuff done:

1.) !help 
To display this message

2.) !rules
To get rules of the ctf


===========Mod Specific Commands================
1.) !ban @username reason
To ban someone

2.) !kick @username reason
To kick someone

3.) !unban username#1234 reason
To unban someone

```
                '''
        await ctx.send(text)

    

    @client.command()
    async def rules(ctx, target):
       rules = '''
```
By playing on this server you agree to these rules:
	1. No swearing, dating, or other inappriopriate behaviour.
	2. No spamming, using all-caps, or any other method of chat abuse.
	3. Don't be a cheater. No hacked clients.
	4. Don't excessively spawnkill. Some spawn killing to stop players chasing
	        the flag bearer is OK, but hogging the flag and repeatedly killing
	        the same players definitely isn't.
	5. Don't be a traitor. Don't:
	    a. Dig blocks in your base to make it less secure or
	       to trap team mates on purpose.
	    b. Help the other team win.
	    c. Change teams.
	6. Don't leave the game whilst in a fight
	7. Don't impersonate other community members.
	8. Do not share your password with ANYONE.
	9. Moderator decisions are final.
```
'''

        await ctx.send(rules)
    

    @client.command()
    async def ping(ctx):
        await ctx.send('Pong!')
    
    @client.command()
    async def bot(ctx):
        await ctx.sne


    @client.command()
    async def clear(ctx,amount=20):
        if "duckie#8881" in str(ctx.message.author) or "Midas#1708" in str(ctx.message.author) :
            await ctx.channel.purge(limit=amount)
        else :
            id = "<@509382450841911307>"
            await ctx.send("Wait a minute, you aint {}".format(id))

        
    @client.command(name="kick")
    @has_permissions(kick_members=True)
    async def _kick(ctx,member: discord.Member, *, reason=None):
        await member.kick(reason=reason)


    @client.command(name="ban")
    @has_permissions(ban_members=True)
    async def _ban(ctx,member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @client.command(name="unban")
    @has_permissions(ban_members=True)
    async def _unban(ctx, *, member):
        a = await ctx.guild.bans()
        name, number = str(member).split('#')
        for i in a:
            if (name,number) == (i.user.name, i.user.discriminator):
                await ctx.guild.unban(i.user)
                await ctx.send(f'The user @{i.user.mention} has been unbanned.')    



event_working()
command_working()
client.run(TOKEN)
