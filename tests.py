from inventory import Inventory
from cart import Cart

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
full = Inventory()
full = Inventory.populate(full, full_inventory)

# #Searching and dealing with just a dictionary
# print (next(item for item in full_inventory if item["qty_dis"] == "True"))

cart = Cart()
left_side = "Inventory"
right_side = "Your cart"
cart_total = "Cart Total"

def addmenu():
    print('\n')
    print(f'{left_side:^40}')
    for c, items in enumerate(full, 0):
        print(f'{c:<3} |   {items["title"]:<20} |   {items["price"]:>7}')

    if len(cart) >= 1:
        print(f'\n \n{right_side:^40}')
        cart.showcart()
        showtotal = cart.calculateTotal()
        print('{:>30}    $ {:.2f}'.format(cart_total, showtotal))

    print("""
            """)

    selectItem()

def remove_menu():
    if len(cart) == 0:
        print("Your cart is empty.  You cannot remove things from an empty cart.")
        pass
    else:
        print(f'\n \n{right_side:^40}')
        cart.showcart()
        showtotal = cart.calculateTotal()
        print('{:>30}    $ {:.2f}'.format(cart_total, showtotal))

        selection = input('''
        To select the item you would like to remove enter its number.
        When you have finished selecting items, type 'pay'.
        To add an item, type 'add'.  
        ''')
        selection = process_selection(selection)
        selection = int(selection)
        cart.removefromcart(selection)
        remove_menu()




def help():
    menuoption = input('''
        If you would like to add items to your cart, type 'add'.
        If you would like to remove an item, type 'remove'.
        If you have selected all of the items you would like to purchase, type 'pay'.
        If you would like to quit, type 'q'.
        To see this in the future enter 'help'.
        \n''')
    menuoption = process_selection(menuoption)
    return menuoption

def payment_screen():
    if len(cart) == 0:
        print("Your cart is empty.  Please add some items before attempting to pay.")
        pass
    else:
        print(f'\n \n{right_side:^40}')
        cart.showcart()
        showtotal = cart.calculateTotal()
        print('{:>30}    $ {:.2f}'.format(cart_total, showtotal))


        return ('b')

def process_selection(menuoption):
    if menuoption == 'add':
        addmenu()
        return
    elif menuoption == 'pay':
        payment_screen()
        return
    elif menuoption == 'remove':
        remove_menu()
        return
    elif menuoption == 'help':
        help()
        return
    else:
        return menuoption




def selectItem():
    selection = input('''
    To select the item you would like to purchase enter its number.
    When you have finished selecting items, type 'pay'.
    To remove an item, type 'remove'.  
    ''')
    if not str.isdigit(selection):
        selection = process_selection(selection)
        return
    else:
        selection = int(selection)
        print(f'You selected {full[selection]["title"]}.')
        cart.addtocart(full, selection)
        addmenu()

# the inititator of the program
quit = None
firsttime = True

while quit != 'q':
    quit = help()


def menu():
    print("""
    
    
    """)
    input
