"Song Lyrics Scraper" 

This project uses a combination of Python's BeautifulSoup, requests and urllib libraries to gather all the songs of an artist from the lyrics website "azlyrics.com". Once gathered, a text file will be generated and each song's lyrics will be appended.

I've included three text files using The Beatles as an example. The beatles_song_list brings together all the links for their song lyrics from the site. 'beatles_lyrics_1' is a small collection of the final output of The Beatles' song lyrics and 'beatles_done' is what has been iterated through.

'getSongList.py' currently contains the entire code for this project. Part I will ask you to enter an artist (spaces and 'The' are removed to comply with the website formatting), and then an artist link will generate, load and save all song links to a text file while cleaning out extraneous links.

Part 2 reads from this text file and then gets the song title and lyrics, cleans them up and appends them to the artist's newly generated text file. It then re-saves the song list minus the current selection and appends that one to a "done" file.

After around 40 iterations in testing, the scraper becomes flagged as a bot by the web site and a captcha pops up. I have yet to implement a get-around to the captcha in code.

As a quick fix for the moment, I've included a second .py file called 'getSong.py' which asks you to input the artist's name you were working on. It will then continue from where you left off in the original file.
