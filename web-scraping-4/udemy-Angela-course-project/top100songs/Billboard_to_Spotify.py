import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


CLIENT_ID = ''
CLIENT_SECRET = ''
HEADER = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}


def get_songs(header, url):
    
    """
    Billboard sitesinden şarkıcıları çeker ve listeler.
    
    Parameters
    ----------
    header : dict
        User-Agent bilgisini barındıran dictionary
    url : str
        Billboard sitesinin linki
    Returns
    -------
    songs_list : list
        Çekilen şarkıcıların listesi
    """
    response = requests.get(url, headers=header)

    try:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser')
    except Exception:
        print(Exception)

    songs = soup.select("h3[class*='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021']")

    songs_list = [f"{i}.{song.get_text(strip=True)}" for i, song in enumerate(songs)]
    return songs_list

def spotify(client_id, client_secret):   
    """
    Spotify API kimlik doğrulama ve oturum açma

    Parameters
    ----------
    client_id : str
        Spotify API client id
    client_secret : str
        Spotify API client secret

    Returns
    -------
    sp : Spotify
        Spotify API objesi
    """

    # Kimlik doğrulama 
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri='https://www.billboard.com/charts/hot-100/',
        scope='user-library-read playlist-read-private playlist-modify-private playlist-modify-public',
    ))

    me = sp.current_user()
    print(me['display_name'])

    return sp

def add_playlist(sp, playlist_id, songs):

    # Şarkı isimlerinden Spotify'da arama yapıp, track id'lerini bul
    track_ids = []
    for song in songs:
        # Şarkı ismini ayıkla (örn: "1. Song Name" -> "Song Name")
        song_name = song.split('.', 1)[-1].strip()
        result = sp.search(q=song_name, type='track', limit=1)
        if result['tracks']['items']:
            track_id = result['tracks']['items'][0]['id']
            track_ids.append(track_id)

    # Şarkıları oynatma listesine ekle
    if track_ids:
        sp.playlist_add_items(playlist_id=playlist_id, items=track_ids)
        print(f"{len(track_ids)} şarkı oynatma listesine eklendi.")
    else:
        print("Hiçbir şarkı bulunamadı veya eklenemedi.")

# KULLANIM
def main():
    year = input("Spotify da hangi tarihin hit şarkılarının listesini oluşturmak istersin? YYYY-MM-DD şeklinde gir.\n")
    URL = f"https://www.billboard.com/charts/hot-100/{year}"

    songs = get_songs(header=HEADER, url=URL)
    print(songs)

    sp = spotify(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user=user_id, name=f"Billboard Top 100 {year}", public=True)
    
    playlist_id = playlist['id']
    add_playlist(sp, playlist_id, songs)


if __name__ == "__main__":
    main()
    