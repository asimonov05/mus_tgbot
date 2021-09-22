from flask.globals import request


import requests

def search(text=None):
    url_search = f'https://page.ligaudio.ru/mp3/{text}'
    res = ['Пустой запрос']
    if text:
        res = requests.get(url_search).text
        res = parse_for_search(res)
    return res

def parse_for_search(search_result=''):
    list_of_tracks = []
    l_tracks = search_result.split('<div class="title">')[1:]
    for i in range(len(l_tracks)):
        track = l_tracks[i]
        track = track[:track.find('</div>')]
        title_len = len('<span class="title" itemprop="name">')
        track_title = track[title_len + 1:track.find('<', title_len)]
        list_of_tracks.append(f'{track_title}')
    return list_of_tracks[:5]