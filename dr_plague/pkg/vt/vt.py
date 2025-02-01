import discord
import os, re, time, json
import requests
import urllib.parse
from datetime import datetime
from table2ascii import table2ascii as t2a, PresetStyle

VT_API_KEY = "e532769887a64ad1ad6aabf7a046ae9177392a0f32f0f72e5d2f16141b652efc"

# Retrieve only the SHA-256 of the matching files
async def get_results(ctx, search, numfiles=5):
	table = []
	url = 'https://www.virustotal.com/api/v3/intelligence/search?'
	headers = {'X-apikey':VT_API_KEY}
	params = urllib.parse.urlencode({'query':search, 'limit':numfiles, 'descriptors_only':'true'})
	url += params

	await ctx.send('[*] Sending search request to VirusTotal.')
	s = requests.Session()
	response = s.get(url, headers=headers)
	responseJSON = json.loads(response.text)
	
	if 'error' in responseJSON:
		await ctx.send("[-] Error:{} Message: {}".format(responseJSON['error']['code'], responseJSON['error']['message']))
		return
	else:
		await ctx.send('[*] Gathering hashes of files returned from search.')
		hashes = []
		embed = discord.Embed(title=f"__**Results:**__", color=0x03f8fc,timestamp= ctx.message.created_at)
		for file in responseJSON['data']:
			hashes.append(file['id'])
			table.append(get_metadata(file['id']))
			res = get_metadata(file['id'])
			embed.add_field(name=f'**Results**',
								value=f'''> SHA1: {res[0]}
										> Name : {res[1]}
										> Size: {res[2]}
										> First Seen: {res[3]}
										> Last Seen: {res[4]}''',
								 inline=False)
	await ctx.send(embed=embed)
	return

async def download_files(ctx, hash_list):
	await ctx.send('[*] Requesting download url for Zip of files from hashes.')
	url = 'https://www.virustotal.com/api/v3/intelligence/zip_files'
	headers = {'X-apikey':VT_API_KEY}
	# Sets Zip file password
	data = json.dumps({"data":{"hashes":hash_list,"password":"infected"}})
	
	ctx.send('[*] Requesting download url for files from VirusTotal.')
	s = requests.Session()
	response = s.post(url=url, headers=headers, data=data)
	responseJSON = json.loads(response.text)
	s.close()

	if 'error' in responseJSON:
		await ctx.send("[-] Error: {} Message: {}".format(responseJSON['error']['code'], responseJSON['error']['message']))
		return
	else:
		download_id = responseJSON['data']['id']
		id_url = 'https://www.virustotal.com/api/v3/intelligence/zip_files/'+download_id
		download_url = 'https://www.virustotal.com/api/v3/intelligence/zip_files/'+download_id+'/download_url'
		
		while True:
			s = requests.Session()
			response = s.get(url=id_url, headers=headers)
			responseJSON = json.loads(response.text)
			s.close()

			if 'error' in responseJSON:
				await ctx.send("[-] Error: {} Message: {}".format(responseJSON['error']['code'], responseJSON['error']['message']))
				return
			else:
				status = responseJSON['data']['attributes']['status']
				if status == 'finished':
					break
		dl_filename = os.path.join('samples','{}.zip'.format(time.strftime('%Y-%m-%dT%H:%M:%S')))
		await ctx.send('[+] Now downloading file {}. Password will be \'infected\'.'.format(dl_filename))
		response = s.get(url=download_url, headers=headers)
		responseJSON = json.loads(response.content)
		s.close()
		
		# Returns a signed URL from where you can download the specified ZIP file. The URL expires after 1 hour.
		zip_url = responseJSON['data']
		response = s.get(url=zip_url, headers=headers)

		if response.status_code == 200:
			# Make subdirectory if needed
			try:
				os.mkdir('samples')
			except:
				pass
			# Write zip file to disk
			download_zip = open(dl_filename, 'wb')
			download_zip.write(bytes(response.content))
			download_zip.close()
		elif 'error' in responseJSON:
			await ctx.send("[-] Error: {} Message: {}".format(responseJSON['error']['code'], responseJSON['error']['message']))
			return
		await ctx.send(file=discord.File(dl_filename))
		s.close()
	return

def get_metadata(file_id):

	metadata = []

	url = 'https://www.virustotal.com/api/v3/files/'
	headers = {'X-apikey':VT_API_KEY}
	
	s = requests.Session()
	response = s.get(url=url+file_id, headers=headers)
	responseJSON = json.loads(response.text)
	s.close()
	
	# Retrieve desired fields
	metadata.append(responseJSON['data']['attributes']['sha1'])
	try:
		metadata.append(responseJSON['data']['attributes']['meaningful_name'])
	except:
		metadata.append("")
	metadata.append(str(responseJSON['data']['attributes']['size']) + ' bytes')
	metadata.append(datetime.utcfromtimestamp(responseJSON['data']['attributes']['first_submission_date']).strftime('%Y-%m-%dT%H:%M:%SZ'))
	metadata.append(datetime.utcfromtimestamp(responseJSON['data']['attributes']['last_submission_date']).strftime('%Y-%m-%dT%H:%M:%SZ'))
	return metadata

# Wrapper for tabulate
#def print_downloads(table):
#	headers = ["SHA-256", "Filename", "Size", "Latest Submission"]
#	print('\nFiles downloaded:\n')
#	print(tabulate(table, headers, showindex=True, tablefmt="grid"))
#	return
