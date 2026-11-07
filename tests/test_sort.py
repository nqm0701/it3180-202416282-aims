import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSortByTitle(unittest.TestCase):
    def test_sort_by_title_ignores_case(self):
        cart = Cart()
        for title in ["apple", "Banana", "cherry"]:
            cart.add_dvd(DigitalVideoDisc(title, "Cat", "Dir", 90, 10.0))
        cart.sort_by_title()
        self.assertEqual([d.title for d in cart.items],
                         ["apple", "Banana", "cherry"])


if __name__ == "__main__":
    unittest.main()
