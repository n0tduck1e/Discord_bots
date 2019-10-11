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
                await i.send('Welcome to **The Rebellion**, {}.\n Type !help to use the bot .\nIntroduce yourself in #general.'.format(member.mention))
    
    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("No Luke, You Must First Become A Jedi")
        else:
            text = '''
```

                    ____
                 _.' :  `._
             .-.'`.  ;   .'`.-.
    __      / : ___\\ ;  /___ ; \\      __
  ,'_ ""--.:__;".-.";: :".-.":__;.--"" _`,
  :' `.t""--.. '<@.`;_  ',@>` ..--""j.' `;
       `:-.._J '-.-'L__ `-- ' L_..-;'
         "-.__ ;  .-"  "-.  : __.-"
             L ' /.------.\\ ' J
              "-.   "--"   .-"
             __.l"-:_JL_;-";.__
          .-j/'.;  ;""""  / .'\"-.
        .' /:`. "-.:     .-" .';  `.
     .-"  / ;  "-. "-..-" .-"  :    "-.
  .+"-.  : :      "-.__.-"      ;-._   \
  ; \\  `.; ;                    : : "+. ;
  :  ;   ; ;                    : ;  : \\:
 : `."-; ;  ;                  :  ;   ,/;
  ;    -: ;  :                ;  : .-"'  :
  :\\     \\  : ;             : \\.-"      :
   ;`.    \\  ; :            ;.'_..--  / ;
   :  "-.  "-:  ;          :/."      .'  :
     \\       .-`.\\        /t-""  ":-+.   :
      `.  .-"    `l    __/ /`. :  ; ; \\  ;
        \\   .-" .-"-.-"  .' .'j \\  /   ;/
         \\ / .-"   /.     .'.' ;_:'    ;
          :-""-.`./-.'     /    `.___.'
                \\ `t  ._  /
                 "-.t-._:'

        
Read the !help, you should
```
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

2.) !resources ML/Hacking/WebDev
To get resources on mentioned fields

3.) !ping
bot replies pong

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
    async def resources(ctx, target):
        ML = '''
``` 
Get basics covered such as:
1.) Learn python libraries such as :
    + numpy : https://numpy.org/
    + pandas : https://pandas.pydata.org/
    + matplotlib : https://matplotlib.org/
Here are some of the resource and blogs on different algorithms. Dividing the algorithm into mainly two parts 
    1. supervised learning  
    2. unsupervised  learning 
    + K-Nearesr Neighbours - https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/
    + Decision Trees - https://homepage.cs.uri.edu/faculty/hamel/courses/2015/spring2015/csc481/lecture-notes/ln481-018.pdf
    + K means clustering - https://www.analyticsvidhya.com/blog/2019/08/comprehensive-guide-k-means-clustering/
    + PCA -https://towardsdatascience.com/a-one-stop-shop-for-principal-component-analysis-5582fb7e0a9c
    + Linear and Logistic Regression -https://towardsdatascience.com/whats-linear-about-logistic-regression-7c879eb806ad

```
'''
        Hacking = '''
```
For getting started in this field, one must have good knowlegde of the following:
1) Networking
    + Read CCNA Routing and Switching Complete Study Guide
    + Get Practical Practice of Networking Protocols
        -> Setup IMAP,POP3,mysql etc servers and play with to get a feel of it
2) Linux FileSystem
    + Download and setup any linux distro in vm and start exploring stuff i.e its filesystem, permissions and default stuff that is present in it.        
    + Practice setting up Networking protocols in this environment.
```
'''

        WebDev = '''Get Cucked
        '''


        if target == "ML":
            await ctx.send(ML)
        elif target == "Hacking":
            await ctx.send(Hacking)
        elif target == "WebDev":
            await ctx.send(WebDev)
    

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
