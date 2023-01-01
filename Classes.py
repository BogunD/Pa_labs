class Item:
    def __init__(self,number,weight,cost):
        self.number = number
        self.weight = weight
        self.price = cost;
    def show_info(self):
        print("Number:", self.number ,", weight:", self.weight, "price:", self.price)
    def get_weight(self):
        return self.weight
    def get_price(self):
        return self.price

class Backpack:
    def __init__(self,capacity,items):
        self.items = items
        self.capacity = capacity
    def get_capacity(self):
        return self.capacity
    def get_items(self):
        return self.items
    def show_info(self):
        print("Capacity:", self.capacity)
        price = 0
        weight = 0
        for item in self.items:
            price += item.get_price()
            weight += item.get_weight()
            item.show_info()
        print("Weight of ALL items:",weight)
        print("Price of ALL items:",price)

    def get_price_list(self):
        l = []
        for item in self.items:
            l.append(item.get_price())
        return l
    def get_weight_list(self):
        l = []
        for item in self.items:
            l.append(item.get_weight())
        return l
