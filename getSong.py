from urllib.parse import quote
import requests
from urllib.request import Request, urlopen
import urllib.parse
urllib.parse.quote(':')
from lxml import etree, html
import re
import time

			
artistName = input("Please type the name of the artist\n")
artistCleaned = artistName.replace(" ", "").replace("the", "")
linkSave = artistCleaned + "_song_list.txt"

# Read links from text file and load them into Py Array
with open(linkSave, "r", encoding="utf-8-sig") as links:
	songLinks = []
	for line in links:
		line = line.replace("\n", "")
		songLinks.append(line)
links.close()
	
# # Parse headers, clean special characters	
# print(songLinks)
lyricSave = artistCleaned + "_lyrics" + ".txt"
linkDone = artistCleaned + "_done" + ".txt"

with open(lyricSave, 'a', encoding='utf_8') as saveLyrics:

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
		print(song_lyrics)

		# Append Lyrics to .Txt File
		spacing = "------------------------------------------------------------\n"
		finalSongFormat = str(song_title) + "\n" + spacing + song_lyrics + "\n" + spacing + "\n\n\n"
		f.write(''.join(finalSongFormat))
	
		# Move link from to-do file to done file
		with open(linkDone, 'a', encoding='utf_8') as songFinished:
			songFinished.write(line  + "\n")
		songFinished.close()
		
		# Resave Song link file - currently finished song. By end this file should be blank and done should be what original lyric file was.
		resaveLinks = open(linkSave).readlines()
		with open(linkSave, "w", encoding="utf-8") as linkResave:
			linkResave.writelines(resaveLinks[1:])
		linkResave.close()
		
saveLyrics.close()	