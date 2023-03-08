# Main file to launch unit tests

from item_test import test_item


def do_test(test, test_name):
    if test:
        print("\033[92m" + str(test_name) + " Passed")
    else:
        print("\033[91m" + str(test_name) + " Failed")


do_test(test_item(), "Item Test")
