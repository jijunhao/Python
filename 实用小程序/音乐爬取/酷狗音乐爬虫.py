import requests
import json
import os, sys
from urllib.request import urlopen
import time
from tqdm import tqdm

timeStamp = (str(time.time())[:-4].replace('.', ''))

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

music_list = []


def GetitemInfo():
    print(
        "\n========================\033[0;36m第一次爬，请先打开URl完成滑动验证\033[0m==========================\n\033[0;36mhttps://www.kugou.com/song/#hash=C9B86DA7FE6F500D72A68FF7A705E1E0&album_id=12855831\033[0m\n")

    search = input("\033[1;45m请输入想搜索的歌\033[0m -==>：")
    url1 = 'https://songsearch.kugou.com/song_search_v2?callback=jQuery112404852453033521309_{}&keyword={}&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_={}'.format(
        timeStamp, search, timeStamp)
    r = requests.get(url1, headers=headers)
    r.encoding = r.apparent_encoding
    slice = input('\n\033[1;32m请进行歌曲筛选，比如：1 ，就是搜索1首歌 ，7 ，就是搜索7首歌。请输入：\033[0m')
    JsonText = json.loads(str(r.text).strip('jQuery112404852453033521309_{}('.format(timeStamp))[:-2])["data"]["lists"][
               0:int(slice) + 1]
    contents1 = []
    tone_quality = input("\n请选择音质；\033[1;45m1\033[0m = 无损音质 ， \033[1;45m2\033[0m = 流畅音质 ， \033[1;45m3\033[0m = 高品音质：")
    if tone_quality == "1":  # 高音质
        for i in JsonText:
            quality_type = {}
            SQFileHash = i['SQFileHash']
            AlbumID = i['AlbumID']
            downurl = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19103604663965204511_{}&hash={}&album_id={}&dfid=3LARt839iuv90cQjCP0QCGCO&mid=bba93f39d313add7dea15367d06ec19d&platid=4&_={}'.format(
                timeStamp, SQFileHash, AlbumID, timeStamp)
            quality_type['type'] = '.flac'
            quality_type['url'] = downurl
            contents1.append(quality_type)

    elif tone_quality == "2":  # 流畅音质
        for i in JsonText:
            quality_type = {}
            AlbumID = i['AlbumID']
            FileHash = i['FileHash']
            downurl1 = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19103604663965204511_{}&hash={}&album_id={}&dfid=3LARt839iuv90cQjCP0QCGCO&mid=bba93f39d313add7dea15367d06ec19d&platid=4&_={}'.format(
                timeStamp, FileHash, AlbumID, timeStamp)
            quality_type['type'] = '.mp3'
            quality_type['url'] = downurl1
            contents1.append(quality_type)

    elif tone_quality == "3":  # 高音质
        for i in JsonText:
            quality_type = {}
            SQFileHash = i['HQFileHash']
            AlbumID = i['AlbumID']
            downurl = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback=jQuery19103604663965204511_{}&hash={}&album_id={}&dfid=3LARt839iuv90cQjCP0QCGCO&mid=bba93f39d313add7dea15367d06ec19d&platid=4&_={}'.format(
                timeStamp, SQFileHash, AlbumID, timeStamp)
            quality_type['type'] = '.mp3'
            quality_type['url'] = downurl
            contents1.append(quality_type)
    else:
        print('接口输入错误：', tone_quality)
        sys.exit()

    return contents1


def parser_json(data):
    ss = 0
    for data in data:
        url = data['url']
        ss += 1
        print('\n', "\033[1;45m=\033[0m" * 36, "\033[1;45m分割线\033[0m", "\033[1;45m=\033[0m" * 36, '\n')
        try:
            response = requests.get(url, headers=headers)
            if 'play_url' in response.text:
                music = {}
                json_TEXt = json.loads(str(response.text).strip("jQuery19108584376284926096_1585328784250(")[:-2])[
                    'data']
                url = json_TEXt['play_url']
                url1 = json_TEXt['play_backup_url']
                music_mane = json_TEXt['album_name']
                singer = json_TEXt['author_name']
                music["音乐链接"] = url
                music["歌曲名字"] = music_mane
                music["歌手"] = singer
                music['歌曲类型'] = data['type']

                print("音乐链接：", url)
                print("备份音乐链接：", url1)
                print("歌曲名字：", music_mane)
                print("歌手：", singer)
                print("下载歌曲的序号：", "\033[1;45m {} \033[0m".format(ss))
                music_list.append(music)

            else:
                print(
                    '\n正在解析歌曲==========================说明：解析后无下载地址是因为该歌曲没有无损音质或需要付费下载==========================\033[31m>>>>>>>如果出现该说明请查看网页是否出现滑动验证<<<<<<<\033[0m')
            continue

        except Exception as e:
            print(e)

    if_download = input("请输入上面的\033[1;45m下载歌曲的序号\033[0m：")

    slice = music_list[int(if_download) - 1:int(if_download)]

    download_from_url(slice)


def download_from_url(music_data):
    for data in music_data:
        url = data['音乐链接']
        music_mane = data['歌曲名字']
        singer = data['歌手']
        quality_type = data['歌曲类型']

        dst = "./music/" + singer + " - " + music_mane + quality_type

        file_size = int(urlopen(url).info().get('Content-Length', -1))

        if os.path.exists(dst):
            first_byte = os.path.getsize(dst)
        else:
            first_byte = 0
        if first_byte >= file_size:
            return file_size
        header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
        pbar = tqdm(
            total=file_size, initial=first_byte,
            unit='B', unit_scale=True, desc=dst)
        req = requests.get(url, headers=header, stream=True)
        with(open(dst, 'ab')) as f:
            for chunk in req.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    pbar.update(1024)
        pbar.close()
        return file_size


if __name__ == '__main__':
    parser_json(GetitemInfo())
