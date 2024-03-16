from celery import shared_task
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from datetime import datetime
# import json
from .models import Menu

def get_cookie_string():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  # Add this line to avoid sandbox issues
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=chrome_options
    )
    print("Driver has been initialized")
    driver.get('https://uci.campusdish.com')
    cookies = driver.get_cookies()
    # driver.quit()
    cookie_string = '; '.join([f"{cookie['name']}={cookie['value']}" for cookie in cookies])
    driver.quit()
    print('passed')
    return cookie_string

def send_request_for_data(cookie_string, period):
    menuWeekDate = datetime.now().strftime("%m/%d/%Y")
    menuWeekDate = "03/15/2024" # this is just for testing
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ko-KR,ko;q=0.9',
        'Cache-Control': 'max-age=0',
        'Cookie': cookie_string,
        'Referer': f'https://uci.campusdish.com/api/menu/GetMenus?locationId=3314&storeIds=&mode=Weekly&date={menuWeekDate}&time=&periodId=&fulfillmentMethod=',
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
    try:
        response = requests.get(f"https://uci.campusdish.com/api/menu/GetMenus?locationId=3314&storeIds=&mode=Daily&date={menuWeekDate}&time=&periodId={period}&fulfillmentMethod=", headers=headers)
    except Exception as e:
        raise Exception("Failed to fetch data")
    if response.status_code != 200:
        raise Exception("Failed to fetch data")
    return response.json()

def parse_data(data):
    n = 0
    for i in data:
        item = i['Product']
        Menu.objects.create(
            name = item['MarketingName'] if item['MarketingName'] != None else "",
            description = item['ShortDescription'],
            period = translate_period(i['PeriodId']),
            containsEggs = item['ContainsEggs'] if item['ContainsEggs'] != None else False,
            containsFish = item['ContainsFish'] if item['ContainsFish'] != None else False,
            containsMilk = item['ContainsMilk'] if item['ContainsMilk'] != None else False,
            containsPeanuts = item['ContainsPeanuts'] if item['ContainsPeanuts'] != None else False,
            containsSesame = item['ContainsSesame'] if item['ContainsSesame'] != None else False,
            containsShellfish = item['ContainsShellfish'] if item['ContainsShellfish'] != None else False,
            containsSoy = item['ContainsSoy'] if item['ContainsSoy'] != None else False,
            containsTreeNuts = item['ContainsTreeNuts'] if item['ContainsTreeNuts'] != None else False,
            containsWheat = item['ContainsWheat'] if item['ContainsWheat'] != None else False,
            isGlutenFree = item['IsGlutenFree'] if item['IsGlutenFree'] != None else False,
            isHalal = item['IsHalal'] if item['IsHalal'] != None else False,
            isKosher = item['IsKosher'] if item['IsKosher'] != None else False,
            isVegan = item['IsVegan'] if item['IsVegan'] != None else False,
            isVegetarian = item['IsVegetarian'] if item['IsVegetarian'] != None else False,
            calories = float(item['Calories']) if isinstance(item['Calories'], str) and item['Calories'].isdigit() else 0.00,
            caloriesFromFat = float(item['CaloriesFromFat']) if isinstance(item['CaloriesFromFat'], str) and item['CaloriesFromFat'].isdigit() else 0.00,
            totalFat = float(item['TotalFat']) if isinstance(item['TotalFat'], str) and item['TotalFat'].isdigit() else 0.00,
            transFat = float(item['TransFat']) if isinstance(item['TransFat'], str) and item['TransFat'].isdigit() else 0.00,
            cholesterol = float(item['Cholesterol']) if isinstance(item['Cholesterol'], str) and item['Cholesterol'].isdigit() else 0.00,
            sodium = float(item['Sodium']) if isinstance(item['Sodium'], str) and item['Sodium'].isdigit() else 0.00,
            totalCarbohydrates = float(item['TotalCarbohydrates']) if isinstance(item['TotalCarbohydrates'], str) and item['TotalCarbohydrates'].isdigit() else 0.00,
            sugars = float(item['Sugars']) if isinstance(item['Sugars'], str) and item['Sugars'].isdigit() else 0.00,
            protein = float(item['Protein']) if isinstance(item['Protein'], str) and item['Protein'].isdigit() else 0.00,
            vitaminA = float(item['VitaminA']) if isinstance(item['VitaminA'], str) and item['VitaminA'].isdigit() else 0.00,
            vitaminC = float(item['VitaminC']) if isinstance(item['VitaminC'], str) and item['VitaminC'].isdigit() else 0.00,
            calcium = float(item['Calcium']) if isinstance(item['Calcium'], str) and item['Calcium'].isdigit() else 0.00,
            iron = float(item['Iron']) if isinstance(item['Iron'], str) and item['Iron'].isdigit() else 0.00,
            saturatedFat = float(item['SaturatedFat']) if isinstance(item['SaturatedFat'], str) and item['SaturatedFat'].isdigit() else 0.00,
            station = translate_station(i['StationId']),
            date = datetime.now()    
            )
        n += 1
    return n

def translate_period(period_num):
    period_dict = {
        "107": "Dinner",
        "49": "Breakfast",
        "106": "Lunch",
        "2651": "Brunch",
        "108": "Late"
        # 1180:
        # 3818:
        # 3819: 
    }
    if period_num not in period_dict:
        return ""
    return period_dict[period_num]

def translate_station(stationId):
    station_dict = {
        "32801": "Grubb/Mainline",
        "32802": "Ember/Grill",
        "32803": "Crossroads",
        "32804": "Honeycakes/Bakery",
        "32805": "The Farm Stand/Salad Bar",
        "32806": "Hearth/Pizza",
        "32807": "Saute",
        "32808": "Soups",
        "32809": "The Farm Stand/Deli",
        "32810": "Vegan",
        "32811": "Compass",
    }
    if stationId not in station_dict:
        return ""
    return station_dict[stationId]

@shared_task
def fetch_and_update_menu():
    cookie_string = get_cookie_string()
    avail_periods = send_request_for_data(cookie_string, "")["Menu"]["MenuPeriods"]
    avail_period_ids = [i["PeriodId"] for i in avail_periods]
    
    total_parsed = 0
    Menu.objects.all().delete()
    for i in avail_period_ids:
        menu_data = send_request_for_data(cookie_string, i)
        menu_items = menu_data['Menu']["MenuProducts"]
        total_parsed += parse_data(menu_items)
    return f"{total_parsed} items have been parsed and updated"

# if __name__ == "__main__":
#     formatted_string = json.dumps(send_request_for_data(get_cookie_string()), indent=2)
#     print(formatted_string)
