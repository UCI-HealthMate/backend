from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from datetime import datetime
import json
from .models import Menu

def get_cookie_string():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=chrome_options.to_capabilities()
    )

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
    menuWeekDate = datetime.now().strftime("%m/%d/%Y")
    response = requests.get(f"https://uci.campusdish.com/api/menu/GetMenus?locationId=3314&storeIds=&mode=Daily&date={menuWeekDate}&time=&49=106&fulfillmentMethod=", headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to fetch data")
    return response.json()

def parse_data(data):
    Menu.objects.all().delete()
    for item in data:
        Menu.objects.create(
            name = item['Name'],
            description = item['ShortDescription'],
            period = translate_period(item['PeriodId']),
            containsEggs = item['ContainsEggs'],
            containsFish = item['ContainsFish'],
            containsMilk = item['ContainsMilk'],
            containsPeanuts = item['ContainsPeanuts'],
            containsSesame = item['ContainsSesame'],
            containsShellfish = item['ContainsShellfish'],
            containsSoy = item['ContainsSoy'],
            containsTreeNuts = item['ContainsTreeNuts'],
            containsWheat = item['ContainsWheat'],
            isGlutenFree = item['IsGlutenFree'],
            isHalal = item['IsHalal'],
            isKosher = item['IsKosher'],
            isVegan = item['IsVegan'],
            isVegetarian = item['IsVegetarian'],
            calories = float(item['Calories']),
            caloriesFromFat = float(item['CaloriesFromFat']),
            totalFat = float(item['TotalFat']),
            transFat = float(item['TransFat']),
            cholesterol = float(item['Cholesterol']),
            sodium = float(item['Sodium']),
            totalCarbohydrates = float(item['TotalCarbohydrates']),
            sugars = float(item['Sugars']),
            protein = float(item['Protein']),
            vitaminA = float(item['VitaminA']),
            vitaminC = float(item['VitaminC']),
            calcium = float(item['Calcium']),
            iron = float(item['Iron']),
            saturatedFat = float(item['SaturatedFat']),
            date = datetime.now()    
        )
    print("Data has been updated")

def translate_period(period_num):
    period_dict = {
        107: "Dinner",
        49: "Breakfast",
        106: "Lunch",
        2651: "Brunch",
        108: "Late Night"
        # 1180:
        # 3818:
        # 3819: 
    }
    return period_dict[int(period_num)]

@shared_task
def fetch_and_update_menu():
    cookie_string = get_cookie_string()
    menu_data = send_request_for_data(cookie_string)
    menu_items = menu_data['Menu']["MenuProducts"]
    parse_data(menu_items)
    


if __name__ == "__main__":
    formatted_string = json.dumps(send_request_for_data(get_cookie_string()), indent=2)
    print(formatted_string)
