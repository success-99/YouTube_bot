# link = "https://youtu.be/8RtPOFUgdiM"

import requests
import json

def youtubemp4(link1):

    link = link1[-11:]

    url = "https://youtube-video-download-info.p.rapidapi.com/dl"

    querystring = {"id": link}

    headers = {
        "X-RapidAPI-Key": "265e2956aemshb14ebbd19ef1c64p17ea0ejsn59bfee97e3b0",
        "X-RapidAPI-Host": "youtube-video-download-info.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    f = response.text
    natija1 = json.loads(f)
    k= natija1['link']
    # print(k.items())
    for d,u in k.items():
        if u[2]=="small":
            return u[0]



    # if 'error' in natija1:
    #     return 'bed'
    # else:
    #     for i in natija1['link']:
    #         for f in i:
    #             print(i.items())
            # if i[2] == 'medium' and i[3] == "360p":
    #             return i[0]

# print(youtubemp4(link))



        # return natija['vidio'][0]
        # return {'vidio': natija['video'][0]}
        # return natija1["formats"][2]['url']
        # for i in natija1['formats']:
        #
        #     if i['format_note'] == '720p' and i['audio_channels'] == 2 and i['asr'] == 44100:
        #         return i['url']
        #     elif i['format_note'] == '480p' and i['audio_channels'] == 2 and i['asr'] == 44100:
        #         return i['url']


# print(youtubemp4(link))
# # if message.text.startswith('https://youtube.be/') or message.text.startswith(
# #         'https://www.youtube.com/') or message.text.startswith('https://youtu.be/'):
# #     link1 = message.text
# #     data2 = youtubedow(link1)
# #     if data2 == "bed":
# #         await message.answer("Hechnarsa topilmadi 😔")
# #     else:
# #         await message.answer_video(data2)
#
#
#
# import json
#
# import requests
#
# #
# # def youtubedow(link):
# #     url = "https://aiov-download-youtube-videos.p.rapidapi.com/GetVideoDetails"
# #
# #     querystring = {"URL": link}
# #
# #     headers = {
# #         "X-RapidAPI-Key": "7452d0fd62msh95c522a9192162dp1c311bjsn64b7eb00230d",
# #         "X-RapidAPI-Host": "aiov-download-youtube-videos.p.rapidapi.com"
# #     }
# #
# #     response = requests.request("GET", url, headers=headers, params=querystring)
# #     natija = json.loads(response.text)
# #     if 'error' in natija:
# #         return 'bed'
# #     else:
# #         for i in natija['link']:
# #             if i[2] == 'medium' and i[3] == "360p":
# #                 return i[0]
# #             elif i['format_note'] == '480p' and i['audio_channels'] == 2 and i['asr'] == 44100:
# #                 return i['url']
# #             elif i['format_note'] == '360p' and i['audio_channels'] == 2 and i['asr'] == 44100:
# #                 return i['url']
# #             elif i['format_note'] == '240p' and i['audio_channels'] == 2 and i['asr'] == 44100:
# #                 return i['url']
# #             elif i['format_note'] == '144p' and i['audio_channels'] == 2 and i['asr'] == 44100:
# #                 return i['url']
# #
#
# #         for i in natija5['formats']:
# #             if i['quality'] == 1:
# #                 return i['url']

# #
# # print(facebook("https://www.facebook.com/100006462294384/videos/583175966256115/"))

#
