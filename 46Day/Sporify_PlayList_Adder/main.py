import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
Client_ID = "8224f143945c4d5c8ee127b1fbc4ab39"
CLIENT_SECRET = "1cafc2ac37654f36848b7915e99fc74e"
date = input("Which year would you like to travel to? Type the date in format of YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/"
response = requests.get(URL + date + "/")
data = response.text
soup = BeautifulSoup(data, "html.parser")
songs = soup.select(selector="li ul li h3", class_="c-title")
titles_of_songs = [song.getText() for song in songs]
for title in titles_of_songs:
    print(title)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

