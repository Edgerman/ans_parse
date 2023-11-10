import requests

url = 'https://prodslms.ilteacher.com/v2/test/getStudentTest'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Authorization': 'Bearer <BEARER_ID>',
    'Content-Type': 'application/json',
    'Origin': 'https://srichaitanyameta.com',
    'Connection': 'keep-alive',
    'Referer': 'https://srichaitanyameta.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'TE': 'trailers',
}

data = {
    'pageLimit': 4,
    'pageNo': 1,
    'testCategory': 1,
    'status': 'UPCOMING'
}

response = requests.post(url, headers=headers, json=data)

t_json = response.json()

# print(t_json['testPapers'])

for x in t_json['testPapers']:
    print(f"[{x['scheduleDetails'][0]['studentTestId']}] ",x['testName'])
