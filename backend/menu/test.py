import requests
import json

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'visid_incap_2829404=HsJG9SR5QXyDa9VejX2yvoXa12UAAAAAQUIPAAAAAABnAB3khoaJAX4SGnP0ZL+N; incap_ses_171_2829404=bU2LNHy1gi4rzrw0A4RfAoXa12UAAAAAtib3tvyVYmZUeg41l5kZbQ==; AramarkContextInfo=32|{a906eb02-9a20-4c32-83ab-4c44aa7ecae2}|Education; __CLAnonymousUser=024GMzBrmBqSNF+hYG8dqz0iw==X9YAW4MS+mw/oLc3vE6zf9/CS0Aox1SQPviBdNlE61gjUDqQasLrFIOvv+Mys0GJO3WpYrxqbbOI2MheyLFeumlFIjqxxYPTzsjuERfU0/wJiZxEL9Ej4OV18LJA+iKwMqi0Y2+HM5a957PQMGuMoTAB/MQx6piuCgYgov/r1gwni9KCCxMJbHnl/3q4Wi7p5znx99rutfvx20h/U1/cts2qrC2vZwpPNjJz70YrVFDfon66EePYWFESdhLbxmDLV1kkIbIwf5sqjwDjc3CyFFwomBpu3xM/8UCm3JIKrbPVVaqPK73T9indEwjc9DaeuGbXBvn4yvN70BXv7gCgQ9MszB741zFnsGxzOWVd1iECNdFrLr5zmaFHFL+yp40wkLTETX92eZkOf6mmzuxO0oq9aonNvzAHtnEqUJzYIcIeq/TvrZI7sBDQxtHO+VkUTZKgbu01s6otP/NxFWX3yDNA7kGtjlVHLAaeS1xGApWwufPvH0T7fPvBG7PYhe8jfB3Nm62Do9BTbKoj/FqWWXoYONLtx90lgNpGlt/hkwR0jDqayTflUF80IHd8nduYg/WKUNJRozlL4X2/m+M6G9FJKkhibF5MCrs0CY5QvfnDTMRk0SvXbNG1q35FfnaFGvdqi4PuHzPVRst+JS9ptwwHbIEzZzL6ORxq61uRMxAs/GlD+SJ/Mwa1+Z0/MpI2R1rOL2a5tzaXC8Hwr7EIcyYQDVQG6znBv6UzL9ZQQSnKjRsOijkagdrmXU7HzNi3HPCb6j1A++88H2mGkvGfaYhptE5leaNfUlY/14rfDT0=',
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
