import requests
from bs4 import BeautifulSoup
import re
import functools
import simplejson as json
import math

with requests.Session() as session:
	
	# get config properties
	with open("config.json") as rawConfig:
		config = json.load(rawConfig)

	# create session
#	session.headers['accept'] = config["session"]["accept"]
	session.headers['cookie'] = config["session"]["cookie"] 
		
	data = session.get('https://' + config["slack-workspace"] + '.slack.com/customize/emoji?page=1', allow_redirects=True).text

	# prepare to parse data
	soup = BeautifulSoup(data, "html.parser")

	# find how many pages there are to scrape
	maxPage = int(functools.reduce(lambda a,b : a if int(a["data-pagination"]) > int(b["data-pagination"]) else b, soup.find_all("a", {"data-pagination": re.compile(r".*")}))["data-pagination"])

	# scrape all emotes
	print("Progress:")
	dataOut = {"count": 0, "fails": 0, "emojis": {}, "failed-urls": [], "workspace": config["slack-workspace"]}
	for i in range(1, maxPage+1):
		print(">", int(math.floor(i/(maxPage+1) * 100)), "%")
		data = session.get('https://ibm-cognitive-engage.slack.com/customize/emoji?page='+str(i), allow_redirects=True).text
		soup = BeautifulSoup(data, "html.parser")

		for elem in soup.find_all("span", {"data-original": re.compile(r".*")}):
			dataOut["count"] += 1
			
			try:
				#print(re.match(r'.*\/(.*)\/.*', elem["data-original"]).group(1))
				dataOut["emojis"][re.match(r'.*\/(.*)\/.*', elem["data-original"]).group(1)] = elem["data-original"]
			except:
				dataOut["failed-urls"].append(elem["data-original"])
				dataOut["fails"] += 1				

	print("You pulled", dataOut["count"], "emojis from", config["slack-workspace"])
	
	try:
		with open(config["outFile"], "w") as outfile:
			outfile.write(json.dumps(dataOut, indent=4))
		outfile.close()
		print("Successfully wrote to", config["outFile"])
	except:
		print("Could not write to", config["outFile"])

