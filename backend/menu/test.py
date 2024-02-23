import requests
import json

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': '_ga_30LZ5B848R=GS1.1.1708727198.1.0.1708727199.59.0.0; _ga_HKPPXV27L6=GS1.1.1708727198.1.0.1708727199.59.0.0; _ga=GA1.1.923277414.1708727198; IsShownMailSubscriptionWidget=1; AramarkContextInfo=32|{a906eb02-9a20-4c32-83ab-4c44aa7ecae2}|Education; shell#lang=en; incap_ses_1287_2829404=JbwZI7+ADzlsMUUrs1jcEZwb2WUAAAAAMv6k1XNITsbfTiUtZ4Bllg==; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+23+2024+14%3A26%3A38+GMT-0800+(Pacific+Standard+Time)&version=6.23.0&isIABGlobal=false&hosts=&consentId=8ecf67b3-bf9c-493a-9dd2-6d8e7b648ee3&interactionCount=0&landingPath=https%3A%2F%2Fuci.campusdish.com%2F&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1; __CLAnonymousUser=024puv8wdwnfO/E0/xc3OV8qg==WSDOV/oIIvbvuKYRjyHk5SS31Fw8E337Qt+EK5xwR1LvoPtgkNWBXVspvZOsTiDvDBg7Kbm41FZgP+PT1ThOltuaHWxgmGPZy67SyOVOMwdschBtR72/Qr+uiKppteRlpHqK3k7h2UpOr246hXIHqQFSyWJOeT6YOWnmrwBZ3eJj3HeIymaiudT5uGTF7quofivDOq4oUPGJ/QOMcTSkHQ10CV9nVM3/HFJG6FbEpqiW76MHLp7HB8u9kluUY+pODd1U8Ew42qUjndqp+BWyrZym7P13UKxfjKMPNcyixJm56hyQ8Yhf0wg205u9ja7kbXkltmN0/LIXADX7WFPrOPJIXjplSbKisJ5rzo+nK55cbjBsSkXIDmUGmyQ/ljgguHREOM0Y5+OH97zapBjReBNmfcjk75lwZcOswCXZsh8KxUjPGMgeqaaDygFWFpnhkmhr5Q7LSVZ9vrCZU4Myc6vchRKABOAvgWYWo1n7btJzVO0P3Gzfzs8Iwt7ESl1uSNZ/180WcbzVBGpAJviTE/JZA20uDkCsTi9DHDjBaBsTzFYAEiWWfpNTTdH2ERAZycuJMzMgkwjAW2ObVqcYVIqWaH4U8Pc84nbwcpJmyO3MABuTQ4OLACvdWtAMwwUN5Cvundj1pyN2DtbSzou2h8jnj2DR9Y3DBQ43SA7ff5oevXY2WcM4BEbLmnXmdarI9jOeLc36SlPtBqrV1Iror29NlgI/mfca9q2ppe5LYl0Nb6jKZNezcKB45n7nWMy5fbhOGi8N6+FjOGEVoXalKP/ZrZgVEb/ASt94vG/EDAY=; _fbp=fb.1.1708727198201.699618652; visid_incap_2829404=MESLOCNRQ5yKF8jPBQlCb5wb2WUAAAAAQUIPAAAAAAAjHZL0xHWmkkI/xlFppz89',
    'Referer': 'https://uci.campusdish.com/api/menu/GetMenus?locationId=3314&storeIds=&mode=Weekly&date=02/19/2024&time=&periodId=106&fulfillmentMethod=',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

response = requests.get("https://uci.campusdish.com/api/menu/GetMenus?locationId=3314&storeIds=&mode=Weekly&date=02/19/2024&time=&periodId=106&fulfillmentMethod=", headers=headers)
formatted_string = json.dumps(response.json(), indent=2)
print(formatted_string)

#107 = monday
#107 = sunday
#1180 = monday
#108 = tuesday
#108 = wednesday
#106 = thursday
#49 = friday
#49 = saturday

# 107 = dinner
# 49 = breakfast
# 106 = lunch
# 2651 = brunch
# 108 = late night
