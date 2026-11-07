import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestFilter(unittest.TestCase):
    def test_filter_by_category(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", "Animation", "Dir", 90, 10.0))
        cart.add_dvd(DigitalVideoDisc("B", "Action", "Dir", 90, 12.0))
        result = cart.filter_by_category("Animation")
        self.assertEqual([d.title for d in result], ["A"])


if __name__ == "__main__":
    unittest.main()
