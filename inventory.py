class Inventory:

    def __init__(self):
        self.products = []

    def populate(self, source):
        for items in source:
            self.products.append(items)

        return self.products

