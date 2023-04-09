"""
-*- coding: utf-8 -*-

@Author : 季俊豪
@Time : 2023/3/20 14:14
@Software: PyCharm 
@File : bilibili.py
"""


import requests
import re
import openai


openai.api_key = ""

def chat(prompt, text):
    completions = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ],
    )
    ans = completions.choices[0].message.content
    return ans

prompt="我希望你是一名专业的视频内容编辑，帮我用中文总结视频的内容精华。我将给你标题、简介、字幕文本，请你将视频内容等进行总结（视频可能没有字幕，字幕中也可能有错别字，如果你发现了错别字请改正）。"

blink = input('请输入B站视频链接：')
bv_pattern = r"/video/([a-zA-Z0-9]+)"
bvid = re.search(bv_pattern,blink).group(1)
print(f'开始处理视频信息：{bvid}')

# 请求获取视频的所有基本信息
url = "https://api.bilibili.com/x/web-interface/view/detail"

params = {"bvid":bvid}
response = requests.get(url,params=params)

video_info = response.json()['data']
title = video_info["View"]["title"]
aid = video_info["View"]["aid"]
desc = video_info["View"]["desc"]
pages = video_info["View"]["pages"]
info = "视频总标题:"+title+";"+"视频简介:"+desc
print("================基础信息=================")
print(title,aid)
print("=================简介================")
print(desc)

# 请求获取cid
cid_list = [page['cid'] for page in pages]
cid_part = [page['part'] for page in pages]

print('==============获取所有章节成功===========')

# 第二次请求获取每章cid的字幕信息
url = 'https://api.bilibili.com/x/player/v2'

cookie = ""

headers = {
            'authority': 'api.bilibili.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.44',
            "cookie":cookie
        }

for i in range(len(cid_list)):

    params = {
                "bvid":bvid,
                "cid":cid_list[i]
              }

    response = requests.get(url, params=params, headers=headers)

    subtitles = response.json()['data']['subtitle']['subtitles']
    if subtitles != []:
        subtitle_url = 'https:'+ subtitles[0]['subtitle_url']
    else:
        subtitle_url = []
        print(f"=======第{i+1}个视频{cid_part[i]}不存在CC字幕==============")

    # 获取这章cid的字幕
    #print(subtitle_url)
    if subtitle_url != []:
        response = requests.get(subtitle_url, headers=headers)

        if response.status_code == 200:
            contents = [x['content'] for x in response.json()['body']]
            content = "。".join(contents)
            print("=============字幕加载成功=============")
            print(content)
    #cid_info = "视频小节标题:" + cid_part[i] +content
    #(chat(prompt, info + cid_info))

            #https://www.bilibili.com/video/BV1TD4y137mP?p=19&vd_source=41955c60a81d9aaae86efb33a72c5101