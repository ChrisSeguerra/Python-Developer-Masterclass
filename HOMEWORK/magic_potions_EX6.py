# The code starts by defining a dictionary 'potions' that stores the available potions and their required ingredients.
# Each key represntts the the potion name and its corresponding value is a list of ingredient names.
potions = {
        "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"],
        "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"],
        "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"]
}

# The 'buy_potion()' function handles the entire process of buying ingredients for a chosen potion.
def buy_potion():
    print("Welcome to the Magic Potion Shop!")
    print ("Available Potions and Ingredients:\n")
    for potion, ingredients in potions.items():
        print(f"\t- {potion}: {ingredients}")
        # Iterates through the potions dictionary and prints the names of 
        # all available potions along with their required ingredients.
    
    # Choosing a potion
    chosen_potion = input("\nEnter the Potion you want to buy: ")
    
    # Validate the chosen potion
    if chosen_potion not in potions:
        print(f"Sorry, we dont have a potion'{chosen_potion}'")
        return
      
    else:
        # Initializing variables and entering the loop:
        ingredients = potions[chosen_potion]
        ingredients_count = 0 

        
        for ingredient in ingredients:

            # Purchasing Ingredients
            while True:
                buy_ingredient = input(f"Do you want to buy {ingredient}? (y/n): ").lower()
                if buy_ingredient == "y":
                    ingredients_count += 1
                    print(f"The ingredient {ingredient} was added to your build.")
                    break
                elif buy_ingredient == "n":
                    print(f"Buying Stopped.")
                    return
                else:
                    print("Invalid input.")
            
            if ingredients_count == 3:
                break

        # Displaying success message
        if ingredients_count == 3:
            print(f"\nCongratulations! You have successfully acquired all the ingredients for the {chosen_potion} potion.")

buy_potion()    


