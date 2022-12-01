import requests
import os

url = 'https://opensea.io/__api/graphql/'
# queryString = {
#     'chain': '',
#     'sortBy': 'ONE_DAY_VOLUME',
#     'timeWindow': 'ONE_DAY'
# }

payload = {
    'id' 'HomePageStatsTablesLazyQuery'
}

# 'accept-encoding': 'gzip, deflate, br',
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US, en; q=0.9',
    'content-length': str(1663),
    'content-type': 'application/json',
    'cookie': 'dpr=2; ajs_anonymous_id=9e1d16e5-76bd-4b89-bf3a-67780e0bab46; _gcl_au=1.1.240965224.1664692524; __os_session=eyJpZCI6IjljZjU1M2Q2LTI1MDYtNDdkNC04ZGEzLTFhNGNjOTQ4NTI0NSJ9; __os_session.sig=_A2K2xeHA7lA9PNjsdiozNyR-QcgtenHRD--3ZYWXDc; muxData=mux_viewer_id=5cce993e-eeda-4e9c-8d89-31bc4a29d9c5&msn=0.01603073893833251&sid=53fcc3a4-f615-4b97-968e-3a2ce0ef3229&sst=1664932173476.5&sex=1664933695314.8; csrftoken=9jdN85zgYlQbH3NcXFKEMbhQj8lG2f2Z; sessionid=eyJzZXNzaW9uSWQiOiI5Y2Y1NTNkNi0yNTA2LTQ3ZDQtOGRhMy0xYTRjYzk0ODUyNDUifQ:1okeWK:HW7KRs3DaXHUy4Bzrk-S8SyGC_eRMmfe-Zrt1OA15yE; assets_card_variant=%22compact%22; _gid=GA1.2.1444387149.1669084639; amp_ddd6ec=CM25uzq-pSlGp6_DVjSS1I...1gigpvq7a.1gigpvs34.1e8.1cg.2qo; _gat_gtag_UA_111688253_1=1; _gat_UA-111688253-1=1; _ga=GA1.1.1579470753.1664692525; _uetsid=96292e506a0e11ed993be7ab6d69c815; _uetvid=6572def0421c11ed9661e394f3cf3240; __cf_bm=qLXF8.d9E6VP5n29.68X4WM83EQhClEVK.7UkDgnZzk-1669158930-0-ASjdb7Smj2QVRYqqnlfFjrr6zdp/NfawQUm/Ah19MF1r4knm1apNc0dOXFr5SqSh5T2nGpwaoxCEr0WNTkjTxRI=; _dd_s=rum=0&expire=1669159849646; _ga_9VSBF2K4BX=GS1.1.1669158924.86.0.1669158949.0.0.0',
    'origin': 'https://opensea.io',
    'referer': 'https://opensea.io/',
    'sec-ch-ua': '"Google Chrome"; v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'x-app-id': 'opensea-web',
    'x-build-id': '3c962e8be8490988c01c8d376147bd1e0055a8a3',
    'x-signed-query': 'af6e7e8669d11b3bd97452519631a37c744f51fea9f98862732db4089305ed46'
}

res = requests.request("POST", url, data = {
        'id': 'HomePageStatsTablesLazyQuery',
        'variables': {
            'sortBy': 'ONE_DAY_VOLUME',
            'chain': 'null',
            'timeWindow': 'ONE_DAY'
        }
    },
    headers = headers)
# print(res.text.encode(encoding = 'UTF-8', errors = 'strict'))
# dec = res.text.encode(encoding = 'UTF-8', errors = 'strict')
# print('')
# print(dec.decode('UTF-8', 'strict'))

if os.path.isfile('openseacollectiondetail.txt'):
    with open('openseacollectiondetail.txt', 'rt') as f:
            etherscanLink = f.readline()
            etherscanLink = etherscanLink[19:]
            print(etherscanLink)
