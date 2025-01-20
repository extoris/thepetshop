import requests

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

params = {
    'direction': 'next',
    'cursor': 'eyJsYXN0X2lkIjo3NTQ5MzYwMDEzMzY1LCJsYXN0X3ZhbHVlIjo3NTQ5MzYwMDEzMzY1fQ==',
    '_data': 'routes/($locale).products._index',
}

response = requests.get('https://www.thepetshop.com/products', params=params, headers=headers)

print(response.text)