from requests import get, RequestException

def main():
    while True:
        category = input("Which type? ").strip().lower()
        if category in ["ingredient", "name", "random"]:
            break
        print("Choose from ingredient, name or random")

    search = "" if category == "random" else input("Enter your search query: ").strip()
    link = check_type(category)
    recipe = return_recipe(link, search)

    if not isinstance(recipe, dict):
        print(recipe)
        return

    for key in recipe:
        print(f"{key} is: {recipe[key]}")

def check_type(c):
    match c:
        case "name":
            return "https://www.themealdb.com/api/json/v1/1/search.php?s="
        case "ingredient":
            return "https://www.themealdb.com/api/json/v1/1/filter.php?i="
        case "random":
            return "https://www.themealdb.com/api/json/v1/1/random.php"

def return_recipe(url, query):
    try:
        response = get(url if query == "" else url + query, timeout=5)
        if response.status_code != 200:
            return "Err... API did not respond properly"
        data = response.json()
        if "meals" not in data or not data["meals"]:
            return "No recipes found"

        meal = data["meals"][0]
        for m in data["meals"]:
            if m.get("strSource"):
                meal = m
                break

    except (RequestException, ValueError, KeyError):
        return "Err... We couldn't get a response, please try again!"

    return format_recipe(meal)

def format_recipe(meal):
    name = meal.get("strMeal", "N/A")
    link = meal.get("strSource", "N/A")
    image = meal.get("strMealThumb", "N/A")

    return {
        "name": name,
        "link": link,
        "image": image
    }


if __name__ == "__main__":
    main()