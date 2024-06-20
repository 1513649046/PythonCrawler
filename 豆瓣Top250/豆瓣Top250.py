import json
import requests
import re
import os

dirs = './data'
if not os.path.exists(dirs):
    os.makedirs(dirs)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'
}


def get_movie_id():
    top250_url = 'https://movie.douban.com/top250?start=0&filter='
    top250_response = requests.get(top250_url, headers=headers)
    top250_movie_id = re.findall('<a href="https://movie.douban.com/subject/(\d{7,8})/">', top250_response.text,
                                 re.S)
    return top250_movie_id


def get_movie_info():
    movie_ids = get_movie_id()
    movie_titles = []
    # print(movie_ids)
    print('开始抓取数据……')
    for movie_id in movie_ids:
        # print(movie_id)
        movie_url = f'https://movie.douban.com/subject/{movie_id}/'
        movie_response = requests.get(movie_url, headers=headers)
        movie_title = re.findall('<span property="v:itemreviewed">(.*?)</span>', movie_response.text, re.S)
        movie_director = re.findall('<a href="/celebrity/\d{7,8}/" rel="v:directedBy">(.*?)</a>', movie_response.text,
                                    re.S)
        movie_type = re.findall('<span property="v:genre">(.*?)</span>', movie_response.text, re.S)
        movie_time = re.findall('<span property="v:initialReleaseDate" content=".*?">(.*?)</span>', movie_response.text,
                                re.S)
        movie_add = re.findall('<span class="pl">制片国家/地区:</span>(.*?)<br/>', movie_response.text, re.S)
        movie_titles.append(movie_title + movie_director + movie_type + movie_time + movie_add)
    return movie_titles


if __name__ == '__main__':
    # print(get_movie_id())
    infos = get_movie_info()
    # with open('./data/info.json', 'w') as f:
    #     json.dump(infos, f)
    with open("./data/info.txt", "w", encoding='UTF-8') as file:
        for item in infos:
            file.write(str(item) + '\n')

    # for info in infos:
    #     print(info)
