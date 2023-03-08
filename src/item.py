class Item:
    def __init__(self, item_id, item_type, item_weight, item_value):
        self.id = item_id           # Item ID, unique ID for each item type
        self.type = item_type       # Item name
        self.weight = item_weight   # Item weight
        self.value = item_value     # Item value

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

    def __str__(self):
        return ("ID       : " + str(self.get_id()) + "\n" +
                "Type     : " + str(self.get_type()) + "\n" +
                "Weight   : " + str(self.get_weight()) + "\n" +
                "Value    : " + str(self.get_value()))
