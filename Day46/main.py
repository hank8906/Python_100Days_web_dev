from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import requests
import spotipy
import os

client_ID = os.environ['client_ID']
client_secret = os.environ['client_secret']
scope = "playlist-modify-private playlist-read-private playlist-modify-public"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_ID,
        client_secret=client_secret,
        redirect_uri='http://example.com',
        scope=scope,
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]
# print(user_id)

travel_date = input('what year you would like to travel to?Type the date in YYY-MM-DD format:')

response = requests.get("https://www.billboard.com/charts/hot-100/" + travel_date)
song_webpage = response.text

soup = BeautifulSoup(song_webpage, "html.parser")
song_selector = soup.select("li ul li h3")

songs = []
for song in song_selector:
    songs.append(song.get_text().strip())
#
# print(songs)

songs_url_list = []
for song in songs:
    # Search for the song on Spotify
    results = sp.search(q=song, type='track', limit=1)

    # Extract the Spotify URI if a match is found
    if results['tracks']['total'] > 0:
        spotify_url = results['tracks']['items'][0]['uri']
        songs_url_list.append(spotify_url)

# print(songs_url_list)

my_play_list = sp.user_playlist_create(user_id,
                                       f"{travel_date} Billboard 100",
                                       public=True,
                                       collaborative=False,
                                       description='YYYY-MM-DD Billboard 100')

sp.playlist_add_items(playlist_id=my_play_list['id'], items=songs_url_list)
