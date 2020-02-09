from bs4 import BeautifulSoup
import requests
import urllib
from urllib.request import Request, urlopen

from urllib.parse import quote
import urllib.parse
urllib.parse.quote(':')

from lxml import etree, html
import re
import time
import sys

############################### Part 1: Gather Song Links ####################################
# Enter Artist Name to generate link
link = "https://www.azlyrics.com/"
artistName = input("Please type the name of the artist\n")
# print(artistName)
artistCleaned = artistName.replace(" ", "").replace("the", "")
linkCleaned = ''.join(link) + artistCleaned[0] + "/" + artistCleaned + '.html'
print(linkCleaned)

# Go to artist's song page and save song links to .txt file
try:
	with urlopen(linkCleaned) as html_page:
		soup = BeautifulSoup(html_page, "lxml")
		linkSave = artistCleaned + "_song_list.txt"
		with open(linkSave, 'w', encoding='utf_8') as saveLinks:
			for link in soup.findAll('a'):
				# print(link.get('href'))
				try:
					saveLinks.write(''.join(link.get('href')) + "\n")
				except:
					print("Empty Href")
		saveLinks.close()
except:
	print("Sorry, lyrics for that entry are not available.")
	sys.exit(1)
		
# clean up href links
with open(linkSave, 'r') as file:
	filedata = file.read()

filedata = filedata.replace("..", "https://www.azlyrics.com")
filedata = filedata.split('\n')

# Save only valid song title links
with open(linkSave, 'w') as fileSave:
	for line in filedata:
		# if not (line.startswith("//") or line.startswith("#") or line.endswith("php") or "facebook.com" in line or "twitter.com" in line or "mailto:?" in line):
		if "https://www.azlyrics.com/lyrics/" in line:
			fileSave.write(line + "\n")
############################### Part I: Complete ####################################





############################### Part 2: Loop Thru Links, Save Lyrics, Format & Append to .Txt ####################################			

# Read links from text file and load them into Py Array
with open(linkSave, "r", encoding="utf-8") as links:
	songLinks = []
	for line in links:
		line = line.replace("\n", "")
		songLinks.append(line)
links.close()
			
# Parse headers, clean special characters	
# print(songLinks)
lyricSave = artistCleaned + "_lyrics" + ".txt"
linkDone = artistCleaned + "_done" + ".txt"

with open(lyricSave, 'w', encoding='utf_8') as saveLyrics:
		
	for line in songLinks:
		# print(line)
		time.sleep(3)
		artistSong = etree.HTML(urlopen(line).read())
		info = requests.get(line)
		# print(info)
		artistSong = html.fromstring(info.content.decode('utf-8', 'ignore'))
		# print(artistSong)
		
		# Get Song Title & Lyrics
		print("***********************************")
		song_title = artistSong.xpath("/html/body/div/div/div/b/text()")
		song_lyrics = artistSong.xpath("/html/body/div/div/div/div[5]/text()")
		
		# Clean Title
		song_title=str(song_title).strip("(\[\'\"|\"\']|\\)")
		print(song_title)
		
		# Clean Lyrics
		song_lyrics=str(song_lyrics)
		lyricsReplace = re.sub(r"(\['|\']|\"]|\\n|\\t|\\x..|\\r|'\r\n)", "", song_lyrics)		
		lyricsReplace2 = re.sub(r"(\", '|\", \"|\', \"|\', ')", "\n", lyricsReplace)
		song_lyrics = str(lyricsReplace2).strip()
		# print(song_lyrics)
		
		# Append to File
		spacing = "------------------------------------------------------------\n"
		finalSongFormat = str(song_title) + "\n" + spacing + song_lyrics + "\n" + spacing + "\n\n\n"
		saveLyrics.write(''.join(finalSongFormat))
		
		# Move link from to-do file to done file
		with open(linkDone, 'a', encoding='utf_8') as songFinished:
			songFinished.write(line  + "\n")
		songFinished.close()
		
		# Resave Song link file - currently finished song. By end this file should be blank
		# and done .txt file should have what original lyric file was.
		resaveLinks = open(linkSave).readlines()
		with open(linkSave, "w", encoding="utf-8") as linkResave:
			linkResave.writelines(resaveLinks[1:])
		linkResave.close()
saveLyrics.close()