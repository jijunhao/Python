from lxml import etree

import requests
url = 'https://music.163.com/#/discover/toplist?id=3778678'
response = requests.get(url)
print(response.text)
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4240.183 Safari/537.36 Edg/85.0.622.63"
}

data = etree.HTML(response.text)
music_list = data.xpath('//a[contains(@href,"/song?")]')
"""
for music in music_list:
    href =  music.xpath('./@href')[0]
    music_id = href.split('=')[1]
    music_name = music.xpath('./text()')[0]

    base_url = 'http://music.163.com/song/media/outer/url?id='
    music_url = base_url + music_id

    music_mp3 = requests.get(music_url,headers=headers)

    with open('./music/%s.mp3' % music_name,'wb') as file:
        file.write(music_mp3.content)
    print("<%s> 下载成功" % music_name)

"""
