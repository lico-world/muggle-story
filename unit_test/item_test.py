from src.item import Item


def test_item():
    # We create an instance of the class Item
    it = Item(0, "Poor Stick", 1, 0)

    # Result we should have
    result = "ID       : " + "0" + "\n" + \
             "Type     : " + "Poor Stick" + "\n" + \
             "Weight   : " + "1" + "\n" + \
             "Value    : " + "0"

    # See if the item str() is the right one
    return str(it) == result
