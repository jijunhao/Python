import requests
import re
from tqdm import tqdm # 进度条展示

url = 'https://vd.l.qq.com/proxyhttp'

# 替换代理池
data = {
    "buid": "vinfoad",
    "adparam": "pf=in&ad_type=LD%7CKB%7CPVL&pf_ex=pc&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200nx1hbcr.html&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fsearch%2F&ty=web&plugin=1.0.0&v=3.5.57&coverid=mzc00200nx1hbcr&vid=j0041h6t8nu&pt=&flowid=ab4b0212035ba32f0451c726691533e7_10201&vptag=film_qq_com%7Cbiu&pu=-1&chid=0&adaptor=2&dtype=1&live=0&resp_type=json&guid=8d8dd8777135690d435d3a63940f15b2&req_type=1&from=0&appversion=1.0.174&uid=1392463115&tkn=3tIsXVEE9Ta9rDqZEEKjuA..&lt=wx&platform=10201&opid=oXw7q0DxYmgHzq--d34WE-llSxk0&atkn=56_JRkecLIuPzzvQyOgsGKMgQu11iuJCd5y86z396Dvh0E_ST1mn4AMNenSIB50DZRnk3v_fugWk1OhQPFNn_cru2FeYQ0KRIwopUSRtv1zCZQ&appid=wxa75efa648b60994b&tpid=1&rfid=869573e667f64486cfed4d7caff19eb7_1650881721",
    "vinfoparam": "spsrt=1&charge=1&defaultfmt=auto&otype=ojson&guid=8d8dd8777135690d435d3a63940f15b2&flowid=ab4b0212035ba32f0451c726691533e7_10201&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.57&host=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200nx1hbcr.html&refer=v.qq.com&sphttps=1&tm=1650883659&spwm=4&logintoken=%7B%22main_login%22%3A%22wx%22%2C%22openid%22%3A%22oXw7q0DxYmgHzq--d34WE-llSxk0%22%2C%22appid%22%3A%22wxa75efa648b60994b%22%2C%22access_token%22%3A%2256_JRkecLIuPzzvQyOgsGKMgQu11iuJCd5y86z396Dvh0E_ST1mn4AMNenSIB50DZRnk3v_fugWk1OhQPFNn_cru2FeYQ0KRIwopUSRtv1zCZQ%22%2C%22vuserid%22%3A%221392463115%22%2C%22vusession%22%3A%223tIsXVEE9Ta9rDqZEEKjuA..%22%7D&vid=j0041h6t8nu&defn=fhd&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&drm=32&hdcp=1&spau=1&spaudio=15&defsrc=2&encryptVer=9.1&cKey=creLV4Dox016KJEItZs_lpJX5WB4a2CdS8kHJaMQVaqtHEZQ1c_W6myJ8hQHnmDFHJgoD52VLzvm2vPBr-xE-uhvZyEMY131vUh1H4pgCXe2Op8F_DerfPItxQA39qtlun0sVBkIXYfWkOdABnbLUo4RgzSXkBHF3N3K7dNKPg_56X9JO3gwBMyBeAex05x8SbbQKY5AXaDVSM7hsBQ8XEeHzIEGJzlCt94ONgPYVSRkZqo51NVr_Bs88Y-USrT0jW_SHLz0xGIJhrZ4JUBeuGEk8zAOhE9HTZPNDViLRIyt2mNDud09qSLLKl4XAj3OFaS3vf_EFS8wguvN7XnVnj5KikwwYNa2JAMiVZKuD8Htx-6y37X14W5WmguS30QBEa1c6w&fp2p=1&spadseg=3"
}


# 替换VIP cookie
headers = {
"cookie": "RK=jakUcpkh2k; ptcz=f8146c89ee21e63c54ec96351e031f974de2c87f1dc250ac7a3663331ad295c6; tvfe_boss_uuid=80ecf6951a850eea; appuser=2221A752E46E80F8; pgv_pvid=916596192; o_cookie=2818657803; pac_uid=1_2818657803; LCZCturn=247; LHTturn=685; ptui_loginuin=1154053620; LBSturn=323; LZCturn=76; LPCZCturn=30; Lturn=514; LKBturn=211; LPVLturn=893; LPLFturn=844; pgv_info=ssid=s7902604745; _qpsvr_localtk=0.04913719518597315; lv_play_index=60; vversion_name=8.2.95; video_omgid=9275f6ef3ec0399d; o_minduid=zxvfTjZfsVrI8ZjLXWuJYF3h5lj12QLv; LPDFturn=415; LPSJturn=893; LVINturn=893; LPHLSturn=136; LPPBturn=47; uid=1140986146",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}

response = requests.post(url=url, json=data, headers=headers)

html_data = response.json()["vinfo"]
print(html_data)

m3u8_url = re.findall("url(.*?),", html_data)[3].split('"')[2]
print(m3u8_url)

pat = re.compile(r'(.+/).+\.ts+')
surl = pat.findall(m3u8_url)[0]
print(surl)

m3u8_data = requests.get(url=m3u8_url,headers=headers).text
print(m3u8_data)

m3u8_data = re.sub('#EXTM3U', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-VERSION:\d', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-MEDIA-SEQUENCE:\d', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-TARGETDURATION:\d+', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-PLAYLIST-TYPE:VOD', '', m3u8_data)
m3u8_data = re.sub('#EXTINF:\d+\.\d+,', '', m3u8_data)
m3u8_data = re.sub('#EXT-X-ENDLIST', '', m3u8_data).split()
print(m3u8_data)

print('======开始下载======')

namestr = input('电影名称是:')
for ts in tqdm(m3u8_data):
    # 替换surl
    ts_url = surl + ts
    ts_content = requests.get(url=ts_url).content
    with open(namestr+'.mp4', mode='ab') as f:
        f.write(ts_content)

print('=====下载完成======')