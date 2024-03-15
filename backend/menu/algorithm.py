def find_menu_combinations(menu_items, target_calories, max_items_per_meal):
    def backtrack(combination, start_index, current_calories):
        if current_calories >= target_calories or len(combination) > max_items_per_meal:
            combinations.append({"total_calories": current_calories, "menu_combination": combination})
            return
        for i in range(start_index, len(menu_items)):
            backtrack(combination + [menu_items[i]], i + 1, current_calories + menu_items[i]["calories"])

    combinations = []
    backtrack([], 0, 0)
    return combinations


def calculate_bmr(sex, height, weight, age, sleep_time, calories_burned):
    if sex == "male":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    elif sex == "female":
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    
    adjusted_bmr = bmr + (calories_burned//2) + (sleep_time * 50)
    return adjusted_bmr

def rank_menu_combinations(combinations, target_calories):
    ranked_combinations = []
    for combination in combinations:
        score = 0
        calorie_difference = abs(target_calories - combination["total_calories"])
        calorie_score = target_calories / calorie_difference
        score += 3 * calorie_score
        
        nutritional_score = (
            combination["protein"] + 
            combination["vitaminC"] + 
            combination["vitaminA"] + 
            combination["calcium"] + 
            combination["iron"] - 
            combination["totalFat"] - 
            combination["transFat"] - 
            combination["cholesterol"] - 
            combination["sodium"] - 
            combination["totalCarbohydrates"] - 
            combination["sugars"] - 
            combination["saturatedFat"]
        )
        score += 0.4 * nutritional_score
        
        ranked_combination = {
            "combination": combination["menu_combination"],
            "calories": combination["total_calories"],
            "score": score
        }
        ranked_combinations.append(ranked_combination)
    
    ranked_combinations.sort(key=lambda x: x["score"], reverse=True)
    
    return ranked_combinations

def distribute_calories_with_brunch(daily_calories):
    breakfast_percentage = 0.30
    brunch_percentage = 0.20
    dinner_percentage = 0.50

    breakfast_calories = daily_calories * breakfast_percentage
    brunch_calories = daily_calories * brunch_percentage
    dinner_calories = daily_calories * dinner_percentage

    return {
        "breakfast": breakfast_calories,
        "brunch": brunch_calories,
        "dinner": dinner_calories,
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
        "breakfast": breakfast_calories,
        "lunch": lunch_calories,
        "dinner": dinner_calories,
        "late_night": late_night_calories
    }

def get_top_3_combinations(ranked_combinations):
    top_3_combinations = []
    for rank in ranked_combinations[:3]:
        top_3_combinations.append(rank["combination"])
    
    # If the length is less than 3, fill the remaining with None
    while len(top_3_combinations) < 3:
        top_3_combinations.append(None)
    
    return top_3_combinations