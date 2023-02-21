# link = "https://youtu.be/rZ0i0uNB10g"

import requests
import json
from environs import Env

env = Env()
env.read_env()

key = env.str("X-RapidAPI_Key")





def youtubedow(link):
    url = "https://aiov-download-youtube-videos.p.rapidapi.com/GetVideoDetails"

    querystring = {"URL": link}

    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "aiov-download-youtube-videos.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    natija = json.loads(response.text)
    ll=natija['title']


    if 'error' in natija:
        return 'bed'
    else:
        for i in natija['formats']:
            if i['format_id'] == "22" and i['asr'] == 44100:
                return i['url'],ll
            elif i['format_id'] == "18" and i['asr'] == 44100:
                return i['url'],ll
            elif i['format_note'] == '240p' and i['audio_channels'] == 2 and i['asr'] == 44100:
                return i['url']
            elif i['format_note'] == '144p' and i['audio_channels'] == 2 and i['asr'] == 44100:
                return i['url']


# print(youtubedow(link))
