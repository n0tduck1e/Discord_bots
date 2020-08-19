#!/usr/bin/env python

import discord
import requests
import time
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
from bs4 import BeautifulSoup
from jikanpy import Jikan
import re

bot = discord.Client()
bot = commands.Bot(command_prefix='senpai ')
bot.remove_command('help')


# making get request in starting so doesnt have make everytime called


r = requests.get('https://thoughtcatalog.com/lorenzo-jensen-iii/2016/11/sick-burns-the-100-greatest-insults-of-all-time/')
soup = BeautifulSoup(r.text,features="html.parser")
a = soup.find('div',{'class':'entry post clearfix'}).find_all('p')

anime_gif = ['https://otakutherapy.com/wp-content/uploads/2016/12/otku_f0320ee0da2348b6.gif','https://media.tenor.com/images/629c31e2b5bdaf0538fbcefc44c6f96b/tenor.gif', 'https://media.tenor.com/images/333c4f19849451c7e1ddff454c9f9372/tenor.gif', 'https://media.tenor.com/images/4a966f2f42658071e5285863350e2549/tenor.gif', 'https://media.tenor.com/images/e2dd904366088f51e30006e46923d1e7/tenor.gif', 'https://media.tenor.com/images/fd0883fee1e08202c2ebefaf2bf6a421/tenor.gif', 'https://media.tenor.com/images/46a74ce6228e7bc535263e1464cce46b/tenor.gif', 'https://media.tenor.com/images/dc58c1ebf66848e9ca48b4a104994470/tenor.gif', 'https://media.tenor.com/images/dff240e0d6e408a6c6b82251ea292a0d/tenor.gif', 'https://media.tenor.com/images/43c516355978f93853ed67c0e2eb455d/tenor.gif', 'https://media.tenor.com/images/18b90c6e3d9bb7f6b9887be466e0931f/tenor.gif', 'https://media.tenor.com/images/72c384cd271aab8a421754a0ab5e42aa/tenor.gif', 'https://media.tenor.com/images/a16bb5057ab1e61654fd7a1213c82dfe/tenor.gif', 'https://media.tenor.com/images/ec5f44a6f93adfa22e36a5c78ae44cdf/tenor.gif', 'https://media.tenor.com/images/4d85ff515cd264eefc0866555a1e9763/tenor.gif', 'https://media.tenor.com/images/ef34332bec620cc4e5fc14fe3d3c4fb6/tenor.gif', 'https://media.tenor.com/images/984ef0d4b7263a409883157810782c9a/tenor.gif', 'https://media.tenor.com/images/4fd49de4149a6d348e04f2465a3970af/tenor.gif', 'https://media.tenor.com/images/4867947603d8200dbe7b7895e97083dc/tenor.gif', 'https://media.tenor.com/images/02860d475dd093a63f4dab49ab99428e/tenor.gif', 'https://media.tenor.com/images/941e523930e326d83664741785231483/tenor.gif', 'https://media.tenor.com/images/de561ea7cda9197ee5817395e44103e1/tenor.gif', 'https://media.tenor.com/images/45a78cb3ad71791ed4973fb157a94af1/tenor.gif', 'https://media.tenor.com/images/62dcb2f6da36a40a6d00104a89f37f92/tenor.gif', 'https://media.tenor.com/images/b919ba80db89baf5334339018dd89f3f/tenor.gif', 'https://media.tenor.com/images/97afa1e615b3f4868ccce48ef8e4e98b/tenor.gif', 'https://media.tenor.com/images/ac941a22610ad462eac0f3b93d55b2a6/tenor.gif', 'https://media.tenor.com/images/8f711b12e00bc1816694bf51909f8b8f/tenor.gif', 'https://media.tenor.com/images/c96d0a36ead6d5d69919bd0b295f58c8/tenor.gif', 'https://media.tenor.com/images/84e609c97fc79323c572baa4e8486473/tenor.gif', 'https://media.tenor.com/images/7738a25f6d810643416f99cdc8a69f2f/tenor.gif', 'https://media.tenor.com/images/804c750d7443635b012b46a65a1e723b/tenor.gif', 'https://media.tenor.com/images/4718e05a77c5561f0e43c5ec0b856608/tenor.gif', 'https://media.tenor.com/images/eece0167331285bca1e22410c5f32f14/tenor.gif', 'https://media.tenor.com/images/56f503e1c49f929fe6f4f2ab33406ba2/tenor.gif', 'https://media.tenor.com/images/006a15fde2af25969b6068bea8267f5c/tenor.gif', 'https://media.tenor.com/images/ed2a3f1a2bdc90840adfbffdd60e2859/tenor.gif', 'https://media.tenor.com/images/e2f50ee7a4c3f9066c3de75aa4ff8d27/tenor.gif', 'https://media.tenor.com/images/f45f5c5fd72dd7c9ff50976e2bc7133c/tenor.gif', 'https://media.tenor.com/images/5928e3641d5f1db32784689901160612/tenor.gif', 'https://media.tenor.com/images/5829c20ecce80dedec8a42537d32292e/tenor.gif', 'https://media.tenor.com/images/bae0f9d28c36037794ec30dcaed11bb7/tenor.gif', 'https://media.tenor.com/images/e3cab802eede8a8bb97defe34a836d5f/tenor.gif', 'https://media.tenor.com/images/df173ddb4338db4c438bd06aa8f180db/tenor.gif', 'https://media.tenor.com/images/e7992ed0535ebf031e2404ea35edc75c/tenor.gif', 'https://media.tenor.com/images/0d4260a30ddf2647a9e1824b8e68defd/tenor.gif', 'https://media.tenor.com/images/876039ded75f425117731ce2a069dd96/tenor.gif', 'https://media.tenor.com/images/8b84daca6dd512a60ed134cfa1f9c086/tenor.gif', 'https://media.tenor.com/images/370f6154ca19d007b49a6ff64344e519/tenor.gif', 'https://media.tenor.com/images/062df15caa058bd703962e8cf1aa385f/tenor.gif','https://media.tenor.com/images/74a2b4b0fc38bc87c81f68b0bb24572d/tenor.gif', 'https://media.tenor.com/images/6f1b243c5d1dca606a2e79d00c62cfce/tenor.gif', 'https://media.tenor.com/images/1255662c238f26f6b19c4ce8a65faa93/tenor.gif', 'https://media.tenor.com/images/f6cdc44b3eb1361bcb421254044323e3/tenor.gif', 'https://media.tenor.com/images/de3ca32f4cea1276c1b9d092ac7a04fe/tenor.gif', 'https://media.tenor.com/images/29642aeb1a9acae4838d8dddfcf96aa1/tenor.gif', 'https://media.tenor.com/images/15a05247ac88d901524adde074651bb6/tenor.gif', 'https://media.tenor.com/images/09bee46d966d658586e8ae3224a7f294/tenor.gif', 'https://media.tenor.com/images/18ec66239b7dcef660b1054f76dc738a/tenor.gif', 'https://media.tenor.com/images/ccce7b14baa959f12861bea455922ae2/tenor.gif', 'https://media.tenor.com/images/018352f0a3b3acc915fa4e8e0accaae5/tenor.gif', 'https://media.tenor.com/images/53a6d2a0e9de9c45cf5391ac749cc6e8/tenor.gif', 'https://media.tenor.com/images/7334ba54f026e086db69577b6193f026/tenor.gif', 'https://media.tenor.com/images/fd175129e200299ec0dba35fcffd87fc/tenor.gif', 'https://media.tenor.com/images/8e1806d2937e8b39eb13c6769d4c77fe/tenor.gif', 'https://media.tenor.com/images/333c4f19849451c7e1ddff454c9f9372/tenor.gif', 'https://media.tenor.com/images/b61766dc8b234fb04b5f6ffc9e3fc76c/tenor.gif', 'https://media.tenor.com/images/cd97cc38633ba0d8d72feea5d66dbb33/tenor.gif', 'https://media.tenor.com/images/1521a5c2ffd10d723309a4ed1b3f0b3d/tenor.gif', 'https://media.tenor.com/images/a23be5d881247f81082cdbdabc69253a/tenor.gif', 'https://media.tenor.com/images/d748d47f3c97b4ac318a0a5573d3b526/tenor.gif', 'https://media.tenor.com/images/777029607cf365f58e8b8ac57d548f19/tenor.gif', 'https://media.tenor.com/images/4e500781edc8e81f75819de379faa9b3/tenor.gif', 'https://media.tenor.com/images/299de89af91aa4f3b77375b4eac5fd56/tenor.gif', 'https://media.tenor.com/images/6665c57af123e46c25195d4bcea1c13b/tenor.gif', 'https://media.tenor.com/images/5b31970652a942f695a58cca59c98216/tenor.gif', 'https://media.tenor.com/images/da4f74ef46f153d472ab5574a17a8410/tenor.gif', 'https://media.tenor.com/images/afac531ed5efdae0e36275e9363ac85f/tenor.gif', 'https://media.tenor.com/images/91d0b45d95b27080c4d0d1175d586533/tenor.gif', 'https://media.tenor.com/images/4e4aca6054a37384ac0beb7f3937cb01/tenor.gif', 'https://media.tenor.com/images/65126e06c4c8ddc1318f3236439297fe/tenor.gif', 'https://media.tenor.com/images/c8f6d1972f6051cf40fec17da7b18a53/tenor.gif', 'https://media.tenor.com/images/8eb3862cfae4553965e88da370c1328c/tenor.gif', 'https://media.tenor.com/images/68048762da94c1158f05f3326f6c9297/tenor.gif', 'https://media.tenor.com/images/e5396fee46afed5947595514348670c9/tenor.gif', 'https://media.tenor.com/images/9e6ad8080e26ee68297ba93f8689ad9b/tenor.gif', 'https://media.tenor.com/images/a2741132a4f7ddf637513737364d87d9/tenor.gif', 'https://media.tenor.com/images/66aa11d3c8ce269440761495c51de6b4/tenor.gif', 'https://media.tenor.com/images/d139e96072bae377be522258f7128881/tenor.gif', 'https://media.tenor.com/images/8b1e91b15f8b3b9f19fb088a7cf8963d/tenor.gif', 'https://media.tenor.com/images/d1c398bfc180d625595ab735dd67192e/tenor.gif', 'https://media.tenor.com/images/569db9df58f58780c169ecfdcc443ca0/tenor.gif', 'https://media.tenor.com/images/b37b59ba5d41216161fe66758f2e8492/tenor.gif', 'https://media.tenor.com/images/f1b9f2523aae5c32ffc7d0c758673711/tenor.gif', 'https://media.tenor.com/images/aea5f4661f18ee280315a7034c63c41a/tenor.gif', 'https://media.tenor.com/images/8729229b46bf9e2756692cfeff94ae64/tenor.gif', 'https://media.tenor.com/images/c99aaa2583769eb8a915588aa4f7db12/tenor.gif', 'https://media.tenor.com/images/b666db38a490638c58fff7def3f13ca1/tenor.gif', 'https://media.tenor.com/images/023f1d2288c9c2b1925099f5aeff7fe6/tenor.gif']

anime_gif2 = ['https://media0.giphy.com/media/wkW0maGDN1eSc/giphy.webp?cid=ecf05e476ff09s0ykrjf4u9gm8cbmyfgnrkiu9wk2ob3p926&rid=giphy.webp','https://media1.giphy.com/media/naiatn5LxTOsU/200w.webp?cid=ecf05e476ff09s0ykrjf4u9gm8cbmyfgnrkiu9wk2ob3p926&rid=200w.webp','https://media1.giphy.com/media/4QxQgWZHbeYwM/200w.webp?cid=ecf05e476ff09s0ykrjf4u9gm8cbmyfgnrkiu9wk2ob3p926&rid=200w.webp','https://media3.giphy.com/media/mf4qECoTz8ZVK/giphy.webp?cid=ecf05e476ff09s0ykrjf4u9gm8cbmyfgnrkiu9wk2ob3p926&rid=giphy.webp','https://media1.giphy.com/media/YZX4FWwOJTK5W/200w.webp?cid=ecf05e476ff09s0ykrjf4u9gm8cbmyfgnrkiu9wk2ob3p926&rid=200w.webp','https://media0.giphy.com/media/o4fyzmHt7DoOI/giphy.webp?cid=ecf05e476ff09s0ykrjf4u9gm8cbmyfgnrkiu9wk2ob3p926&rid=giphy.webp','https://giphy.com/gifs/Alissandra-Sementilli-anime-tokyo-ghoul-fZ93CIL1OtOVmDJ0X7','https://media1.giphy.com/media/bMLGNRoAy0Yko/200w.webp?cid=ecf05e47wko65g0j4wkzdoj997xoeqt1nq9y5v8iicb79499&rid=200w.webp','https://media3.giphy.com/media/UYzNgRSTf9X1e/200w.webp?cid=ecf05e47efjbtpy09fy0g0t5gopgwdpo6l1usls82yu7pn5a&rid=200w.webp','https://media2.giphy.com/media/3o7btMCltyDvSgF92E/200w.webp?cid=ecf05e472ohvip7ni662o6cq8go5vx8g8pqw8w6t21wihjjd&rid=200w.webp','https://media2.giphy.com/media/l0IxZkXQw9A7OqbbW/200w.webp?cid=ecf05e472ohvip7ni662o6cq8go5vx8g8pqw8w6t21wihjjd&rid=200w.webp','https://media1.giphy.com/media/2SnmQg8DrZzHy/200w.webp?cid=ecf05e4739zxisgkgbbodvqpg97ec6cwbpmla038892anmz1&rid=200w.webp','https://media3.giphy.com/media/4pk6ba2LUEMi4/200w.webp?cid=ecf05e4739zxisgkgbbodvqpg97ec6cwbpmla038892anmz1&rid=200w.webp','https://media1.giphy.com/media/NlpnSfpBdjwxG/200w.webp?cid=ecf05e4712klfkvndv5058ax4mgqe4lhm78xeyy7i0mh9b6e&rid=200w.webp','https://media0.giphy.com/media/d0JPBhiwCm6Kk/200w.webp?cid=ecf05e47q1qjyrxvlplrqdibswxfwj7xy5l3d12u0zu3d6j7&rid=200w.webp','https://media2.giphy.com/media/kNBLrv3JiDKw/200w.webp?cid=ecf05e47q1qjyrxvlplrqdibswxfwj7xy5l3d12u0zu3d6j7&rid=200w.webp']

anime_gif = anime_gif + anime_gif2

def nhentai_fetch(number):
	url = "https://nhentai.net/g/" + str(number) + "/"
	r = requests.get(url)
	c = re.compile('https://t.nhentai.net/galleries/[0-9]*/cover.[a-zA-Z]*')
	return (c.findall(r.text)[0])




def message_lister():
	@bot.event
	async def on_ready():
		print("Bot is ready to be used\n")

	@bot.event
	async def on_message(message):
		if message.author == bot.user:
			pass
		elif "69" in message.content:
			await message.channel.send('Nice desu UwU')
		
		key_words = {'hard','long','deep','all day long','do this all day','dick','big'}
		for i in key_words:
			if i in message.content:
				await message.channel.send('thats what she said')
				break
		await bot.process_commands(message)
	
	@bot.event
	async def on_command_error(ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("What are you doing, senpai?")
			await ctx.send("You dont have permission on this server")
		else:
			await ctx.send("Bakadesu ka? Read !help ")
	@client.event
    async def on_member_join(member : discord.Member):
        for i in member.guild.channels:
            if str(i) == "welcome":
                await i.send('Welcome to **PwnBpit**, {}.\n Type !help to use the bot.'.format(member.mention))

def command_working():

	@bot.command(name="help")
	async def help(ctx):
		help = '''
```
Konichiwa ! OwO

I am LegalLoli, talking to me definitely wont get your name on FBI watch list UwU.
Use the following commands:

senpai help => see this message again

senapi insult => get a random insult, you pathetic weeb

senpai top_anime <rank> => Get all time top anime rank specific. (Defaults to top 10)
	ex senpai top_anime 12

senpai seasonal <rank> => Seasonal anime rank specific. (Defaults to top 10)
	ex senpai seasonal 12

senpai animegif => Random anime gif

senpai waifu => coming soon, pervert.

senpai clear <number> => Delete Messages (Default 20)
	ex senpai clear 6

senpai nhentai <number> => get cover page of given "manga" UwU (NSFW)
	ex senpai nhentai 323257

------- Mod Specific Commands -------

senpai ban <member tag> <reason>
		ex senpai ban @duckie too leet

senpai unban <member tag>
		ex senpai unban @duckie

senpai kick <member> <reason>
		ex senpai kick @vatsal too weeb


Thats it. Bie Bye UwU !
```
'''
		if "Yup_That_Guy#2104" in str(ctx.message.author):
			await ctx.send('No help for you, weeb')
		else:
			await ctx.send(help)

	@bot.command()
	async def top_anime(ctx,rank=9999):
		jk = Jikan()
		top_anime = jk.top(type="anime")['top']
		if rank != 9999:
			if rank > len(top_anime):
				await ctx.send('baka, only top 50 exists')
			else:
				rank = rank -1
				data = "{} \n\nName: {}\nRank: {}\nMovie\nScore {}".format(top_anime[rank]['image_url'],top_anime[rank]['title'],top_anime[rank]['rank'],top_anime[rank]['score'])
				await ctx.send(data)
		else:

			for i in range(10):
				if top_anime[i]['episodes'] == 1:
					data = "{} \n\nName: {}\nRank: {}\nMovie\nScore {}".format(top_anime[i]['image_url'],top_anime[i]['title'],top_anime[i]['rank'],top_anime[i]['score'])
				else:
					data = "{} \n\nName: {}\nRank: {}\nEpisodes: {}\nScore: {}".format(top_anime[i]['image_url'],top_anime[i]['title'],top_anime[i]['rank'],top_anime[i]['episodes'],top_anime[i]['score'])
				await ctx.send(data)
	
	@bot.command()
	async def seasonal(ctx,rank=9999):
		jk = Jikan()
		anime = jk.season(year=2020,season='summer')['anime']
		if rank != 9999:
			rank = rank -1
			if rank > len(anime):
				await ctx.send('baka, Only {} new anime this summer'.format(len(anime)))
			else:
				data = "{} \n\nName: {}\nScore: {}\nEpisodes: TBA\n".format(anime[rank]['image_url'],anime[rank]['title'],anime[rank]['score'])
				await ctx.send(data)
		else:
			for i in range(10):
				if anime[i]['episodes'] == None:
					data = "{} \n\nName: {}\nScore: {}\nEpisodes: TBA\n".format(anime[i]['image_url'],anime[i]['title'],anime[i]['score'])
				else:
					data = "{} \n\nName: {}\nScore: {}\nEpisodes: {}\n".format(anime[i]['image_url'],anime[i]['title'],anime[i]['score'],anime[i]['episodes'])
				await ctx.send(data)


	@bot.command()
	async def clear(ctx,amount=20):
			#if "duckie#8881" in str(ctx.message.author):
			await ctx.channel.purge(limit=amount)
			

	@bot.command()
	async def waifu(ctx):
		r = requests.get('https://boards.4channel.org/c/')
		c = re.compile('//[a-z0-9A-z]\.4cdn.org/c/[0-9a-zA-Z]+[^s]\.[a-zA-Z]+')
		a = c.findall(r.text)
		print (len(a))
		rnd = random.randint(0,len(a))
		await ctx.send('https:' + a[rnd])
	
	@bot.command()
	async def loli(ctx):
		a = ['/wp/wp4747935.jpg', '/wp/wp4747935.jpg', '/wp/wp2263080.jpg', '/wp/wp2263080.jpg', '/wp/wp4747930.png', '/wp/wp4747930.png', '/wp/wp4747933.jpg', '/wp/wp4747933.jpg', '/wp/wp4747935.jpg', '/wp/wp4747935.jpg', '/wp/wp4747936.png', '/wp/wp4747936.png', '/wp/wp4747940.jpg', '/wp/wp4747940.jpg', '/wp/wp4747942.png', '/wp/wp4747942.png', '/wp/wp4747943.jpg', '/wp/wp4747943.jpg', '/wp/wp4747944.png', '/wp/wp4747944.png', '/wp/wp4747948.jpg', '/wp/wp4747948.jpg', '/wp/wp4747952.jpg', '/wp/wp4747952.jpg', '/wp/wp4729482.jpg', '/wp/wp4729482.jpg', '/wp/wp4747954.jpg', '/wp/wp4747954.jpg', '/wp/wp4034215.jpg', '/wp/wp4034215.jpg', '/wp/wp4747957.jpg', '/wp/wp4747957.jpg', '/wp/wp4747958.jpg', '/wp/wp4747958.jpg', '/wp/wp4747963.jpg', '/wp/wp4747963.jpg', '/wp/wp4747965.jpg', '/wp/wp4747965.jpg', '/wp/wp4747966.jpg', '/wp/wp4747966.jpg', '/wp/wp4747969.jpg', '/wp/wp4747969.jpg', '/wp/wp4747970.jpg', '/wp/wp4747970.jpg', '/wp/wp4249502.jpg', '/wp/wp4249502.jpg', '/wp/wp4747972.jpg', '/wp/wp4747972.jpg', '/wp/wp4747975.png', '/wp/wp4747975.png', '/wp/wp4747979.jpg', '/wp/wp4747979.jpg', '/wp/wp4747980.jpg', '/wp/wp4747980.jpg', '/wp/wp4729449.jpg', '/wp/wp4729449.jpg', '/wp/wp4747982.jpg', '/wp/wp4747982.jpg', '/wp/wp4747985.jpg', '/wp/wp4747985.jpg', '/wp/wp4747986.jpg', '/wp/wp4747986.jpg', '/wp/wp4747989.jpg', '/wp/wp4747989.jpg', '/wp/wp4747991.jpg', '/wp/wp4747991.jpg', '/wp/wp4747994.jpg', '/wp/wp4747994.jpg', '/wp/wp4747995.jpg', '/wp/wp4747995.jpg', '/wp/wp4729450.jpg', '/wp/wp4729450.jpg', '/wp/wp4747998.jpg', '/wp/wp4747998.jpg']
		
		rnd = random.randint(0,len(a))
		await ctx.send('https://wallpapercave.com/' + a[rnd])
	
	@bot.command()
	async def nhentai(ctx,number=-1):
		if number == -1:
			await ctx.send("Add the magic number to get a result, senpai UwU")
			await ctx.send("Usage !nhentai 323257")
		else:
			await ctx.send(nhentai_fetch(number))

	
	@bot.command()
	async def animegif(ctx):
		c = random.randint(0,99)
		await ctx.send(anime_gif[c])

	@bot.command()
	async def insult(ctx):
		c = random.randint(0,100)
		await ctx.send(a[c].text)


######### MOD SPECIFIC COMMANDS ####################


	@bot.command(name="kick")
	@has_permissions(kick_members=True)
	async def _kick(ctx,member: discord.Member, *, reason=None):
		await member.kick(reason=reason)
		

	@bot.command(name="ban")
	@has_permissions(ban_members=True)
	async def _ban(ctx,member: discord.Member, *, reason=None):
		await ctx.send('https://media.tenor.com/images/a2aa57ff88350e16f501a3a5f43fb0a1/tenor.gif')
		await ctx.send("user banned desu")
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

	
	

	bot.run('-key-here-')

message_lister()
command_working()