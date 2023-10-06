import os

try:
	from pytube import Playlist
	from art import *
except ModuleNotFoundError:
	os.system('pip install pytube')
	os.system('pip install art')
tprint("URLBOT")
print("Developed by charan champ")
print("-----------------------------")

def get_playlist(playlists):
	urls = []
	for playlist in playlists:
		playlist_urls = Playlist(playlist)

		for url in playlist_urls:
			urls.append(url)

	return urls
input_string = input("Enter the playlist url separated by space: ")

playlist = input_string.split(" ")
#playlist = ['https://www.youtube.com/watch?v=25LgJzG2Fg0&list=PL0nX4ZoMtjYFJ-A-7LsrN0C0-HXpf2scV']

pl_urls = get_playlist(playlist)

with open('pl_urls.txt','w') as f:
	for url in pl_urls:
		f.write(url+'\n')

print("urls successfully saved into "+ os.getcwd()) 
