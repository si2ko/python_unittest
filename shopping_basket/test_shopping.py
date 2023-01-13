import unittest
from basket import ShoppingBasket

class TestShoppingBasketWithOutProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket()

    def test_size_of_basket_should_be_empty(self):

        self.assertEqual(len(self.basket),0)

    def test_getting_product_out_of_range_should_raise_error(self):

        self.assertRaises(IndexError, self.basket.get_product,2)

    def test_total_amount_should_be_zero(self):

        self.assertEqual(0, self.basket.total())

class TestShoppingBasketWithOneProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket().add_product('milk',3)

    def test_size_of_basket_should_be_one(self):

        self.assertEqual(len(self.basket),1)

    def test_total_amount(self):

        self.assertEqual(3.63, self.basket.total())

    def test_getting_product(self):

        self.assertEqual(self.basket.get_product(0), self.basket.products[0])

    def test_getting_product_out_of_range(self):

        self.assertRaises(IndexError, self.basket.get_product,2)

class TestShoppingBasketWithTwoProducts(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.basket = ShoppingBasket().add_product('milk',3).add_product('water',2)

    def test_size_of_basket_should_be_one(self):

        self.assertEqual(len(self.basket),2)

    def test_order(self):

        self.assertEqual('milk',self.basket.get_product(0).name)
        self.assertEqual('water', self.basket.get_product(1).name)

    def test_total_amount(self):

        self.assertEqual(self.basket.total(),6.05)

    def test_getting_product_out_of_range(self):

        self.assertRaises(IndexError, self.basket.get_product,2)
