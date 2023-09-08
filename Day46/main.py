from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import requests
import spotipy

client_ID = "ae41b55336cc479e89307ede3e3be670"
client_secret = "eba3d7f64ce94cbd9e8cbeed59701ae0"
scope = "playlist-modify-private"

auth = SpotifyOAuth(
    client_id=client_ID,
    client_secret=client_secret,
    redirect_uri='http://example.com',
    scope=scope,
)


endpoint = "https://api.spotify.com/v1/users/11164799549/playlists"



body = {
    "name": "New Playlist",
    "description": "New playlist for Billboard top 100",
    "public": False
}

playlist_response = requests.post(url=endpoint, json=body)
print(playlist_response.text)

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])




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