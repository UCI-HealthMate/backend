from django.forms.models import model_to_dict

def find_menu_combinations(menu_items, target_calories, max_items_per_meal, max_combinations=50):
    combinations = []
    def backtrack(combination, start_index, current_calories, combinations):
        if len(combinations) >= max_combinations or current_calories >= target_calories or len(combination) > max_items_per_meal:
            combinations.append({"total_calories": current_calories, "menu_combination": combination})
            return
        for i in range(start_index, len(menu_items)):
            backtrack(combination + [menu_items[i]], i + 1, current_calories + menu_items[i].calories, combinations)

    backtrack([], 0, 0, combinations)
    return combinations


def calculate_bmr(sex, height, weight, age, sleep_time, calories_burned):
    if sex == "male":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    elif sex == "female":
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    
    adjusted_bmr = bmr + (calories_burned) + (sleep_time * 50)
    return adjusted_bmr * 9

def rank_menu_combinations(combinations, target_calories):
    ranked_combinations = []
    for combination in combinations:
        score = 0
        calorie_difference = abs(target_calories - float(combination["total_calories"]))
        calorie_score = target_calories / calorie_difference
        score += 7000 * calorie_score
        for item in combination["menu_combination"]:
            menu_dict = model_to_dict(item)
            nutritional_score = (
                menu_dict['protein'] + 
                menu_dict['vitaminC'] + 
                menu_dict['vitaminA'] + 
                menu_dict['calcium'] + 
                menu_dict['iron']
            )
            score += 0.4 * float(nutritional_score)
        menu_combination_dict = [
            model_to_dict(menu_item) for menu_item in combination["menu_combination"]
        ]
        ranked_combination = {
            "combination": menu_combination_dict,
            "calories": combination["total_calories"],
            "score": score
        }
        ranked_combinations.append(ranked_combination)
    ranked_combinations.sort(key=lambda x: x["score"], reverse=True)
    print("processed one ranked combination")
    return ranked_combinations

def distribute_calories_with_brunch(daily_calories):
    breakfast_percentage = 0.30
    brunch_percentage = 0.20
    dinner_percentage = 0.50

    breakfast_calories = daily_calories * breakfast_percentage
    brunch_calories = daily_calories * brunch_percentage
    dinner_calories = daily_calories * dinner_percentage

    return {
        "Breakfast": breakfast_calories,
        "Brunch": brunch_calories,
        "Dinner": dinner_calories,
    }

def distribute_calories_with_late(daily_calories):
    breakfast_percentage = 0.25
    lunch_percentage = 0.35
    dinner_percentage = 0.3
    late_night_percentage = 0.1

    breakfast_calories = daily_calories * breakfast_percentage
    lunch_calories = daily_calories * lunch_percentage
    dinner_calories = daily_calories * dinner_percentage
    late_night_calories = daily_calories * late_night_percentage

    return {
        "Breakfast": breakfast_calories,
        "Lunch": lunch_calories,
        "Dinner": dinner_calories,
        "Late": late_night_calories
    }

def get_top_3_combinations(ranked_combinations):
    top_3_combinations = [0]*3
    for i in range(len(ranked_combinations)):
        top_3_combinations[i] = ranked_combinations[i]["combination"]
        if i == 2:
            break  
    for i in range(3):
        if top_3_combinations[i] == 0:
            top_3_combinations[i] = None
    
    return top_3_combinations