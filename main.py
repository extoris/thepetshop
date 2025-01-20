import json
import re
import requests
from bs4 import BeautifulSoup
import csv


NEXT_PAGE = True


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return (self.name, self.price)    

def get_sourse(url, params):
    cookies = {
        '_shopify_y': 'ca302c19-F4BA-4AE2-57E7-28DC47AE14D7',
        'session': 'eyJleHByZXNzRGVsaXZlcnlEYXRhIjp7Imdsb2JhbEZsYWciOnRydWUsImV4cHJlc3NEZWxpdmVyeUF2YWlsYWJsZSI6ZmFsc2UsImxvY2FsV2FyZWhvdXNlSWQiOm51bGx9LCJsb2NhbFdhcmVob3VzZSI6eyJsb2NhbFdhcmVob3VzZUlkIjpudWxsLCJmb3JtYXR0ZWRBZGRyZXNzIjpudWxsLCJzZWxlY3RlZEFkZHJlc3NDb29yZGluYXRlcyI6bnVsbCwibG9jYWxXYXJlaG91c2VJc09wZW4iOmZhbHNlLCJleHByZXNzRGVsaXZlcnlBdmFpbGFibGUiOmZhbHNlfX0%3D.I%2F2h9tUmjNb2ZM8g03dvxJ8cwrtPbL6URs6bzW9%2F%2B8M',
        '__cf_bm': 'btE4H1juNOJ4j3R9vtVUNNHQf8DWUAW1wkKwNp3Zxps-1737300633-1.0.1.1-XeENNNcWZ4oS1P7r2PRsv2qTSGaD2hVs.UIRzBZtzdzLcM3TK5YnKu66Hhk_vYK1kpttxPGDjhE6Rr0hUsW9Cw',
        '_shopify_s': '7f2ff8b1-8068-472F-5DF4-E8A09615680C',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:134.0) Gecko/20100101 Firefox/134.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://www.thepetshop.com/products?direction=next&cursor=eyJsYXN0X2lkIjo3NTQ5NDMzMDg2MDA1LCJsYXN0X3ZhbHVlIjo3NTQ5NDMzMDg2MDA1fQ%3D%3D',
        'DNT': '1',
        'Alt-Used': 'www.thepetshop.com',
        'Connection': 'keep-alive',
        # 'Cookie': '_shopify_y=ca302c19-F4BA-4AE2-57E7-28DC47AE14D7; session=eyJleHByZXNzRGVsaXZlcnlEYXRhIjp7Imdsb2JhbEZsYWciOnRydWUsImV4cHJlc3NEZWxpdmVyeUF2YWlsYWJsZSI6ZmFsc2UsImxvY2FsV2FyZWhvdXNlSWQiOm51bGx9LCJsb2NhbFdhcmVob3VzZSI6eyJsb2NhbFdhcmVob3VzZUlkIjpudWxsLCJmb3JtYXR0ZWRBZGRyZXNzIjpudWxsLCJzZWxlY3RlZEFkZHJlc3NDb29yZGluYXRlcyI6bnVsbCwibG9jYWxXYXJlaG91c2VJc09wZW4iOmZhbHNlLCJleHByZXNzRGVsaXZlcnlBdmFpbGFibGUiOmZhbHNlfX0%3D.I%2F2h9tUmjNb2ZM8g03dvxJ8cwrtPbL6URs6bzW9%2F%2B8M; __cf_bm=btE4H1juNOJ4j3R9vtVUNNHQf8DWUAW1wkKwNp3Zxps-1737300633-1.0.1.1-XeENNNcWZ4oS1P7r2PRsv2qTSGaD2hVs.UIRzBZtzdzLcM3TK5YnKu66Hhk_vYK1kpttxPGDjhE6Rr0hUsW9Cw; _shopify_s=7f2ff8b1-8068-472F-5DF4-E8A09615680C',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'Priority': 'u=0',
    }

    response = requests.get(url, params=params, headers=headers)

    return response

    # with open("json.html", "w") as file:
    #     file.write(response.text)

    # soup = BeautifulSoup(response.text, "lxml")
 
    # with open("sourse.html", "r") as file:
    #     response = file.read()
    # soup = BeautifulSoup(response, "lxml")

    # return soup
    

def get_json(sourse):
    print('get_json')
    try:
        soup = BeautifulSoup(sourse.text, "lxml")
        script = soup.find(string=re.compile('window.__remixContext')).split(';')[0].split('Context = ')[-1].strip()
        data = json.loads(script)
        products = data['state']['loaderData']['routes/($locale).products._index']
    except AttributeError:
        products = {}
        print('NO JSON DATA')
    return products


def get_params(data): 
    params = {
        'direction': 'next',
        'cursor': data["products"]["pageInfo"]["endCursor"],
        '_data': 'routes/($locale).products._index',
    }   
    return params

def next_page(data, NEXT_PAGE):
    NEXT_PAGE = data["products"]["pageInfo"]["hasNextPage"]

def get_answer(data):
    answer = []
    list_items = data['products']['nodes']
    for title in list_items:
        for variant in title["variants"]["nodes"]:
            item = Item(name = variant["product"]["title"],
                        price= variant["price"]["amount"])
            answer.append(item)
    with open('items.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for item in answer:
            writer.writerow([item.name, item.price])


def main():
    url = 'https://www.thepetshop.com/products'
    sourse = get_sourse(url, params=None)
    data = get_json(sourse)
    params = get_params(data)
    get_answer(data)
    while NEXT_PAGE:        
        data = get_sourse(url, params)
        get_answer(data)
        params = get_params(data)
        next_page(data, NEXT_PAGE)
        

if __name__ == '__main__':
    main()
