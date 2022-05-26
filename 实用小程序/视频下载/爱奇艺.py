import requests
import re
from tqdm import tqdm # 进度条展示

url = ['https://data.video.iqiyi.com.8old.cn/m3u8cache/iqiyi/966470b15891ee26c308074d2182be71.m3u8',
       'https://data.video.iqiyi.com.8old.cn/m3u8cache/iqiyi/da47164c09a38a70c02708c6bf5e8221.m3u8',
       ]


print('======开始下载======')

for i in range(len(url)):
    response = requests.get(url=url[i])
    html_data = response.text
    pat = re.compile(r'http.+')
    surl = pat.findall(html_data)
    for ts in tqdm(surl):
        ts_content = requests.get(url=ts).content
        with open('觉醒年代'+str(i+1)+'.mp4', mode='ab') as f:
            f.write(ts_content)
    print("第"+str(i+1)+"集完成")
print('=====下载完成======')


