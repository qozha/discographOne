import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from dotenv import load_dotenv
from methods import create_discographone_playlist, get_discographone_playlist

load_dotenv()


auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)


scope = 'playlist-modify-public'
spoty = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

name = input("Enter name: ")

tracks = get_discographone_playlist(spoty, name)


if create_discographone_playlist(spoty, tracks, name):
    print("Done! ")
