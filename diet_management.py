# Diet Management System
items = {
    #Protein(g),Carbohydrates(g),Fat(g),Calories(kcal)
    "Apple":(0.003,0.138,0.002,0.52),
    "Banana":(0.011,0.228,0.003,0.89),
    "Cauliflower":(0.019,0.050,0.003,0.25),
    "Spinach":(0.029,0.036,0.004,0.23),
    "Broccoli":(0.028,0.066,0.004,0.34),
    "Almonds":(0.212,0.216,0.499,5.79),
    "Lentils (Raw)":(0.246,0.634,0.011,3.52),
    "Chickpeas (Raw)":(0.205,0.630,0.060,3.78),
    "Tofu":(0.080,0.019,0.048,0.76),
    "Oats":(0.169,0.663,0.069,3.89),
    "Quinoa (Raw)":(0.141,0.642,0.061,3.68),
    "Brown Rice (Raw)":(0.079,0.772,0.029,3.70),
    "Potato":(0.020,0.175,0.001,0.77),
    "Tomato":(0.009,0.039,0.002,0.18),
    "Carrot":(0.009,0.096,0.002,0.41),
    "Cucumber":(0.007,0.036,0.001,0.15),
    "Walnuts":(0.152,0.137,0.652,6.54),
    "Peanuts":(0.258,0.161,0.492,5.67),
    "Orange":(0.009,0.118,0.001,0.47),
    "Grapes":(0.007,0.181,0.002,0.69)

}
def main():
    print("Diet Management System")
    n_items = int(input("Enter the number of items you have eaten: "))
    protein = 0
    carbohydrates = 0
    fat = 0
    calories = 0

    for i in range(n_items):
        food = input("Enter the name of the item: ").title()
        if food in items:
            print("Item found")
            quntity = int(input("Enter the quantity of the item(g): "))
            protein += items[food][0] * quntity
            carbohydrates += items[food][1] * quntity
            fat += items[food][2] * quntity
            calories += items[food][3] * quntity

        else:
            print("Item not found")
    print("Total Protein(g):", protein)
    print("Total Carbohydrates(g):", carbohydrates)
    print("Total Fat(g):", fat)
    print("Total Calories(kcal):", calories)

if __name__ == "__main__":
    main()
