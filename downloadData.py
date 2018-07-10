import urllib.request
import json
import re
import signal
import time

try:
	with open('config.json') as rawConfig:
		config = json.load(rawConfig)
except:
	print("Counldn't open config.json, you sure the file is there?")
	sys.exit()
try:
	with open(config["outFile"]) as rawData:
		data = json.load(rawData)
except:
	print("Couldn't open", config["outFile"], "you sure the file is there?")
	sys.exit()

print("Starting in 3 seconds")
time.sleep(3)
for emoji in data["emojis"]:
	link = data["emojis"][emoji]
	try:
		ext = re.match(r'.*(\..*)', link).group(1)
		filepath = "./emojis/" + str(emoji) + str(ext)
		urllib.request.urlretrieve(link, filepath)
		print("> Downloaded", emoji, "from", link)
	except:
		print("!!!> Could not download", emoji, "from", link)

