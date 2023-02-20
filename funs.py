
def fun1(natija):
    if 'error' in natija:
        return 'bed'
    else:
        for i in natija['formats']:
            if i['qualityLabel'] == "720p":
                return i['url']


def fun2(natij):
    if 'error' in natij:
        return 'bed'
    else:
        for i in natij['formats']:
            if i['qualityLabel'] == "360p":
                return i['url']