import re
import time
import requests
from unidecode import unidecode
from bs4 import BeautifulSoup, UnicodeDammit
from html import unescape
import sys

def song_find():
    try:
        songs, artists = get_info_spotify()
        return [songs, artists]
    except Exception:
        return "spotify is off"

def get_info_spotify():
    import win32gui
    windows = []
    old_window = win32gui.FindWindow("SpotifyMainWindow", None)
    old = win32gui.GetWindowText(old_window)
    def find_spotify_uwp(hwnd, windows):
        text = win32gui.GetWindowText(hwnd)
        classname = win32gui.GetClassName(hwnd)
        if classname == "Chrome_WidgetWin_0" and len(text) > 0:
            windows.append(text)
    if old:
        windows.append(old)
    else:
        win32gui.EnumWindows(find_spotify_uwp, windows)
    if len(windows) == 0:
        pass

    try:
        artist, track = windows[0].split(" - ", 1)
    except ValueError:
        artist = ''
        track = windows[0]
    except IndexError:
        pass

    if windows[0].startswith('Spotify'):
        return ['Spotify',""]

    return track, artist
def get_lyrics(song, artist) :

    urls = stripper(song,artist)

    try:
        url = f'https://genius.com/{urls}-lyrics'
        page = requests.get(url)
        page.raise_for_status()
    except requests.exceptions.HTTPError:
        return "lyric was not found."
    html = BeautifulSoup(page.text, "html.parser")
    lyrics_path = html.find("div", class_="lyrics")
    if lyrics_path:
        lyrics = UnicodeDammit(lyrics_path.get_text().strip()).unicode_markup
    else:

        lyrics_path = html.find_all("div", class_=re.compile("^Lyrics__Container"))
        lyrics_data = []
        for x in lyrics_path:
            lyrics_data.append(UnicodeDammit(re.sub("<.*?>", "", str(x).replace("<br/>", "\n"))).unicode_markup)

        lyrics = "\n".join(unescape(lyrics_data))
    return lyrics


a = re.compile(r'([(\[](feat|ft|From "[^"]*")[^)\]]*[)\]]|- .*)', re.I)
b = re.compile(r'[^ \-a-zA-Z0-9]+')
c = re.compile(' *- *| +')
d = re.compile(r'(?: *\(with )([^)]+)\)')
e = re.compile(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]')
def stripper(song,artist):
    song = re.sub(a, '', song).strip()
    ft = d.search(song)
    if ft:
        song = song.replace(ft.group(), '')
        ar = ft.group(1)
        if '&' in ar:
            artist += f'-{ar}'
        else:
            artist += f'-and-{ar}'
    song_data = artist + '-' + song

    url_data = song_data.replace('&', 'and')

    url_data = url_data.replace('/', ' ').replace('!', ' ').replace('_', ' ')
    for ch in ['Ø', 'ø']:
        url_data = url_data.replace(ch, '')
    url_data = re.sub(e, '', url_data)
    url_data = unidecode(url_data)
    url_data = re.sub(b, '', url_data)
    url_data = re.sub(c, '-', url_data.strip())
    return url_data

def main():
    flag = None
    while True:
        song_info = song_find()

        if song_info[0] != flag and song_info[1] != '':

            print(f"song name: {song_info[0]} artist: {song_info[1]}",get_lyrics(song=song_info[0], artist=song_info[1].split(",")[0]),sep= "\n")

            flag = song_info[0]
        time.sleep(0.3)

if __name__ == '__main__':
    print("Designed by Bahadir")
    main()

