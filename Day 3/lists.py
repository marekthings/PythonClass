ingredients = ["Mushrooms", "Onions", "Red Pepper", "Cheese", "Spinach"]
print (ingredients)
userinput = input("Add Ingredient")
ingredients.append(userinput)
print (ingredients)

RemoveIngredient = input("Select one to remove")
ingredients.remove(RemoveIngredient)
print(ingredients)

ingredients.sort()
print(ingredients)