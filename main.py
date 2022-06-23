import requests
from datetime import datetime

header = {
    # "authority": "glados.rocks",
    # "method": "POST",
    # "path": "/api/user/checkin",
    # "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "content-type": "application/json;charset=UTF-8",
    "cookie": '_ga=GA1.2.876969835.1654698637; _gid=GA1.2.1075006440.1655782461; '
              'koa:sess=eyJ1c2VySWQiOjE1NTc4NCwiX2V4cGlyZSI6MTY4MTcwMjU5MTczNiwiX21heEFnZSI6MjU5MjAwMDAwMDB9; '
              'koa:sess.sig=0Goj0cWuxibbrwTSCQOD8OMxsFo; _gat_gtag_UA_104464600_2=1',
    "origin": "https://glados.rocks",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
    "sec-ch-ua-mobile": '?0',
    "sec-ch-ua-platform": '"Windows"',
    'sec-fetch-dest': 'empty',
    "sec-fetch-mode": 'cors',
    "sec-fetch-site": "same-origin"
}

sendcodePayload = {
    "address": "504024159@qq.com",
    "site": "glados.network"
}

token ={
    "token": "glados.network"
}

r = requests.post("https://glados.rocks/api/user/checkin", headers=header, json=token)
# r1 = requests.post("https://glados.rocks/api/user/status", headers=header)
print(r.content)
print(len(r.content))