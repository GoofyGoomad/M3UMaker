import os
from pathlib import Path
import sys
import codecs
from codecs import decode

acceptedCodecs = (".wav", ".flac", ".mp3", ".opus", ".ogg")

print("Enter music playlist directory")
playlistDirectory = input("")
playlistPath = Path(playlistDirectory)
print("Going to " + playlistDirectory + "...")

print("What is the playlist name")
playlistName = input("")

os.chdir(playlistPath)

musicFiles = []

for file in playlistPath.iterdir():
	#print("Found " + file)
	if file.is_file() and (str(file)).endswith(acceptedCodecs):
		print("Adding " + (str(file)) + "...")
		with open(playlistName + '.m3u', 'w') as playlist:
			musicFiles.append(str(file))

with open(playlistName + '.m3u', 'w', encoding="utf-8") as playlist:
	playlist.write("#EXTM3U\n")
	playlist.write("#PLAYLIST:" + playlistName + "\n")
	for files in musicFiles:
		playlistPathString = str(playlistPath)
		encodedMusicFile = playlistPathString.encode("utf-8")
		decodedMusicFile = encodedMusicFile.decode("utf-8")
		individualFile = files.replace((str(playlistPath) + "\\"), "")
		playlist.write(individualFile + "\n")
		print(individualFile + " - Music track added successfully!")