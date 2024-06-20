# 爬取网易云歌曲

import requests  # 数据请求
import re  # 正则表达式
import os  # 创建文件夹 文件操作

filename = 'music\\'
if not os.path.exists(filename):  # 判断是否有文件夹
    os.mkdir(filename)
# 修改榜单id可以爬取其他榜单
url = 'https://music.163.com/discover/toplist?id=2149107400'
# headers请求头，将python代码伪装成浏览器访问服务器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
                  'Safari/537.36'
}
response = requests.get(url=url, headers=headers)
# print(response.text)
html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)
for num_id, title in html_data:
    # 获取音乐接口
    music_url = f'https://music.163.com/song/media/outer/url?id={num_id}.mp3'
    # 对音乐播放地址发送请求 获取二进制数据内容
    music_content = requests.get(url=music_url, headers=headers).content
    # 保存
    with open(filename + title + '.mp3', mode='wb') as f:
        f.write(music_content)
    print(num_id, title)