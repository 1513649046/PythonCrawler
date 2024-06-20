import requests
from bs4 import BeautifulSoup
import csv


def get_jd_daily_supplies(keyword):
    url = f"https://search.jd.com/Search?keyword={keyword}&enc=utf-8"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    items = soup.find_all('div', class_='gl-i-wrap')

    results = []

    for item in items:
        name = item.find('div', class_='p-name').text.strip()
        price = item.find('strong').text.strip()
        link = item.find('div', class_='p-img').find('a')['href']
        results.append({'name': name, 'price': price, 'link': link})

    return results


def save_to_csv(items, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'price', 'link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow(item)


if __name__ == "__main__":
    keyword = input("请输入要搜索的日用品关键词：")
    items = get_jd_daily_supplies(keyword)

    filename = f"{keyword}_jd_daily_supplies.csv"
    save_to_csv(items, filename)
    print(f"日用品信息已保存到文件: {filename}")
