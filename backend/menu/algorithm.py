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


def calulate_bmr(sex, height, weight, age, sleep_time, calories_burned):
    if sex == "male":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    elif sex == "female":
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    
    adjusted_bmr = bmr + (calories_burned//2) + (sleep_time * 50)
    return adjusted_bmr

def rank_menu_combinations(combinations):
    ranked_combinations = []
    for combination in combinations:
        rank = {
            "combination": combination["menu_combination"],
            "calories": combination["total_calories"],
            "score": 0
        }
        for item in combination:
            score = (
                item["protein"] + 
                item["vitaminC"] + 
                item["vitaminA"] + 
                item["calcium"] + 
                item["iron"] - 
                item["totalFat"] - 
                item["transFat"] - 
                item["cholesterol"] - 
                item["sodium"] - 
                item["totalCarbohydrates"] - 
                item["sugars"] - 
                item["saturatedFat"]
            )
            rank["score"] += score
        ranked_combinations.append(rank)
    
    ranked_combinations.sort(key=lambda x: x["score"], reverse=True)
    
    return ranked_combinations