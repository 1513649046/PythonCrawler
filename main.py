# # 这是一个示例 Python 脚本。
#
# # 按 Shift+F10 执行或将其替换为您的代码。
# # 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#
#
# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按装订区域中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'
}

movie_url = f'https://movie.douban.com/subject/1292052/'
movie_response = requests.get(movie_url, headers=headers)
# print(movie_response.text)
# movie_time = re.findall('<span property="v:initialReleaseDate" content=".*?">(.*?)</span>', movie_response.text, re.S)
movie_type = re.findall('<span property="v:genre">(.*?)</span>', movie_response.text, re.S)
movie_type = eval(str(movie_type).replace(',', '').replace(' ', ''))
print(movie_type)
# ['剧情', '犯罪']
