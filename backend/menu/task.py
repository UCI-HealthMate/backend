from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

def get_cookie_string():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://uci.campusdish.com')
    cookies = driver.get_cookies()
    driver.quit()
    cookie_string = '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    return cookie_string

def send_request_for_data(cookie_string):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9',
        'Cache-Control': 'max-age=0',
        'Cookie': cookie_string,
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
    return response.json()

@shared_task
def fetch_and_update_menu():
    cookie_string = get_cookie_string()
    menu_data = send_request_for_data(cookie_string)
    
