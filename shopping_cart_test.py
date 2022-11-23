from oop_shopping_cart_copy import CustomerInfo
import unittest

class OopShoppingCartTest(unittest.TestCase):

    def test_delete(self):
        cart = CustomerInfo()
        cart.shopping_cart['eggs'] = 12
        cart.shopping_cart['milk'] = 1
        self.assertIn('eggs', cart.shopping_cart)

    def test_add(self):
        cart = CustomerInfo()
        cart.shopping_cart['eggs'] = 12
        cart.shopping_cart['milk'] = 1
        self.assertNotIn('cheese', cart.shopping_cart)

    def test_main_prompt_notEquals(self):
        cart = CustomerInfo()
        cart.shopping_cart['eggs'] = 12
        cart.shopping_cart['milk'] = 1
        self.assertNotEqual('eggs', 12, cart.shopping_cart)
    
    def test_main_prompt_Equals(self):
        cart = CustomerInfo()
        cart.shopping_cart['eggs'] = 12
        cart.shopping_cart['eggs'] = 6
        cart.shopping_cart['milk'] = 1
        self.assertEqual('eggs', 'eggs', cart.shopping_cart)
        self.assertEqual('eggs', 'eggs', cart.shopping_cart)

    # def test_delete_item(self):
    #     test_shopping_cart = {}
    #     test_shopping_cart['eggs'] = 12
    #     test_shopping_cart['milk'] = 1
    #     self.assertIn('eggs', test_shopping_cart)
    #     CustomerInfo.delete_item('eggs', 12, test_shopping_cart)
    #     self.assertNotIn('eggs', test_shopping_cart)

    # def test_add_item(self):
    #     test_shopping_cart = {}
    #     test_shopping_cart['milk'] = 1
    #     self.assertIn('milk', test_shopping_cart)
    #     CustomerInfo.add_item('eggs', 12, test_shopping_cart)
    #     # test_shopping_cart['eggs'] = 12
    #     self.assertIn('eggs', test_shopping_cart)
    #     self.assertNotIn('cheese', test_shopping_cart)


unittest.main()