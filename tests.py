from inventory import Inventory

full_inventory =[
    {
        "title": "Bottled Water",
        "imagepath": "img/products/bottledwater.gif",
        "price": "0.50",
        "alt" : "16 ounce bottle of water",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },

    {
        "title": "Frappuccino",
        "imagepath": "img/products/frap.gif",
        "price": "1.00",
        "alt" : "12 ounce bottle of Frappuccino",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },


    {
        "title": "Gatorade",
        "imagepath": "img/products/gatorade.gif",
        "price": "1.00",
        "alt" : "16 ounce bottle of Gatorade",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },

    {
        "title": "Monster Energy",
        "imagepath": "img/products/monster-energy.gif",
        "price": "2.00",
        "alt" : "16 ounce can of Monster Energy drink",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },

    {
        "title": "Monster Energy x2",
        "imagepath": "img/products/monster-energy2.gif",
        "price": "3.50",
        "alt" : "16 ounce cans of Monster Energy drink",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },

    {
        "title": "Soda",
        "imagepath": "img/products/soda.gif",
        "price": "0.50",
        "alt" : "12 oz can of Soda",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },

    {
        "title": "Tea",
        "imagepath": "img/products/tea.gif",
        "price": "1.00",
        "alt" : "16 ounce bottle of tea",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },

    {
        "title": "Vitamin Water",
        "imagepath": "img/products/vitamin-water.gif",
        "price": "1.00",
        "alt" : "16 ounce bottle of Vitamin Water",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },

    {
        "title": "Blow Pop",
        "imagepath": "img/products/blowpop.gif",
        "price": "0.25",
        "alt" : "Bag Animal Crackers",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },

    {
        "title": "Laffy Taffy (3)",
        "imagepath": "img/products/laffy-taffy.gif",
        "price": "0.25",
        "alt" : "12 ounce bottle of Apple Juice",
        "qty_dis": "False",
        "min_dis_qty": "",
        "qty_price": ""
    },

    # {
    #     "title": "Candy Bar",
    #     "imagepath": "img/products/kitkat.gif",
    #     "price": "1.00",
    #     "alt" : "A single candy bar",
    #     "qty_dis": "False",
    #     "min_dis_qty": "",
    #     "qty_price": ""
    # },
    #
    # {
    #     "title": "Candy Bar x 2",
    #     "imagepath": "img/products/2candy.gif",
    #     "price": "1.50",
    #     "alt" : "2 candy bars",
    #     "qty_dis": "False",
    #     "min_dis_qty": "",
    #     "qty_price": ""
    # },
    #
    # {
    #     "title": "Banana Bread",
    #     "imagepath": "img/products/Banana-Bread.gif",
    #     "price": "0.50",
    #     "alt" : "A package of crackers",
    #     "qty_dis": "False",
    #     "min_dis_qty": "",
    #     "qty_price": ""
    # },
    #
    # {
    #     "title": "Chips",
    #     "imagepath": "img/products/chips.gif",
    #     "price": "0.50",
    #     "alt" : "10 oz bag of chips",
    #     "qty_dis": "False",
    #     "min_dis_qty": "",
    #     "qty_price": ""
    # },
    #
    # {
    #     "title": "Cinnamon Roll",
    #     "imagepath": "img/products/Cinnamon-Rolls.gif",
    #     "price": "1.00",
    #     "alt" : "A cinnamon roll",
    #     "qty_dis": "False",
    #     "min_dis_qty": "",
    #     "qty_price": ""
    # },
    #
    # {
    #     "title": "Cookies",
    #     "imagepath": "img/products/cookie.gif",
    #     "price": "0.50",
    #     "alt" : "A big yummy cookie",
    #     "qty_dis": "False",
    #     "min_dis_qty": "",
    #     "qty_price": ""
    # },
    #
    # {
    #     "title": "Crackers",
    #     "imagepath": "img/products/crackers.gif",
    #     "price": "0.50",
    #     "alt" : "A package of crackers",
    #     "qty_dis": "False",
    #     "min_dis_qty": "",
    #     "qty_price": ""
    # },
    #
    # {
    #     "title": "Granola Bar",
    #     "imagepath": "img/products/granola.gif",
    #     "price": "0.50",
    #     "alt" : "A granola bar",
    #     "qty_dis": "False",
    #     "min_dis_qty": "",
    #     "qty_price": ""
    # },
    #
    # {
    #     "title": "Peanuts",
    #     "imagepath": "img/products/peanuts.gif",
    #     "price": "0.75",
    #     "alt" : "A package of peanuts",
    #     "qty_dis": "False",
    #     "min_dis_qty": "",
    #     "qty_price": ""
    # },

    {
        "title": "Pickle",
        "imagepath": "img/products/dill-pickle.gif",
        "price": "1.00",
        "alt" : "A Pickle",
        "qty_dis": "True",
        "min_dis_qty": "2",
        "qty_price": "0.35"

    },

    {
        "title": "Rice Krispy Treat",
        "imagepath": "img/products/ricetreat.gif",
        "price": "0.50",
        "alt" : "A Rice Krispy Treat",
        "qty_dis": "True",
        "min_dis_qty": "",
        "qty_price": ""
    }
]
full=Inventory()
full = Inventory.populate(full, full_inventory)

# #Searching and dealing with just a dictionary
# print (next(item for item in full_inventory if item["qty_dis"] == "True"))

print('\n')

for c, items in enumerate(full, 0):
    print(f'{c:<3} |   {items["title"]:<20} |   {items["price"]:>8}')

selection = int(input('Choose which item you would like to purchase: '))

print(f'You selected {full_inventory[selection]["title"]}.')

confirm = input(f'Add {full_inventory[selection]["title"]} to your cart? y/n')

if confirm == 'y':
    print(f'{full_inventory[selection]["title"]} successfully added to cart.')
else:
    print('Well, alright then.  Bye.')

