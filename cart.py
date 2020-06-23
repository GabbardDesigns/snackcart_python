class Cart:

    def __init__(self):
        self.cart = []

    def __len__(self):
        return len(self.cart)

    def addtocart(self, inventory, selection):

        confirm = input(f'Add {inventory[selection]["title"]} to your cart? (y/n)  ')

        if confirm == 'y':
            print(f'{inventory[selection]["title"]} successfully added to cart.')
            self.cart.append(inventory[selection])
        else:
            print('Well, alright then.  Bye.')

    def removefromcart(self, selection):

        confirm = input(f'Remove cart[selection]["title"] from your cart? (y/n)  ')
        #
        # if confirm == 'y':
        #     print(f'{inventory[selection]["title"]} successfully added to cart.')
        #     self.cart.append(inventory[selection])
        # else:
        #     print('Well, alright then.  Bye.')


    def calculateTotal(self):
        total = 0.00
        for c, items in enumerate(self.cart, 0):
            total += float(items["price"])
        return total

    def showcart(self):
        for c, items in enumerate(self.cart, 0):
            print(f'{c:<3} |   {items["title"]:<20} |   {items["price"]:>8}')
