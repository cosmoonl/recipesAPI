import requests
def recipe_search(ingredient, health):
    app_id=''
    app_key=''
    url = 'https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}&health={}'.format(ingredient, app_id, app_key, health)
    result = requests.get(url)
    data = result.json()
    return data['hits']

def run():
    ingredient = input("Enter an ingredient: ")
    health = input("What is your diet? ")
    results = (recipe_search(ingredient, health))
    recipes = []

    for result in results:
        recipes.append(result['recipe'])

    recipes = sorted(recipes, key=lambda x: x['calories'])


    for recipe in recipes:
        print()
        print(recipe['label'])
        print(recipe['dietLabels'])
        print("Number of portion: {}".format(int(recipe['yield'])))
        print("This recipe contains {} calories.".format(int(recipe['calories'])))
        Calorie_per_portion = int(recipe['calories'])/int(recipe['yield'])
        print("Calories per portion: {:.0f}".format(Calorie_per_portion))
        print("Suitable for: {}".format(recipe['healthLabels']))
        print(recipe['image'])
        print()

    with open('recipes.txt', 'w+') as text_file:
        for result in recipes:
            text_file.write(str(result['label']) + '\n')
            text_file.write(str(result['dietLabels']) + '\n')
            text_file.write('{:.0f}'.format(result['yield']) + ' portions'+'\n')
            text_file.write('{:.0f}'.format(result['calories']) + ' calories'+ '\n')
            text_file.write(str(result['url']) + '\n')
            text_file.write(str(result['healthLabels']) + '\n')
            text_file.write('\n')

run()


