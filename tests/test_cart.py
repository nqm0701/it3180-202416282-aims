   import unittest
   from types import SimpleNamespace
   from aims.cart import Cart


   def make_dvd(cost=1.0):
       return SimpleNamespace(title="Disc", cost=cost)


   class TestCart(unittest.TestCase):
       def test_add_dvd_until_full(self):
           cart = Cart()
           for _ in range(20):
               self.assertTrue(cart.add_dvd(make_dvd()))
           self.assertFalse(cart.add_dvd(make_dvd()))

       def test_total_cost(self):
           cart = Cart()
           cart.add_dvd(make_dvd(10.0))
           cart.add_dvd(make_dvd(20.0))
           self.assertAlmostEqual(cart.total_cost(), 30.0)


   if __name__ == "__main__":
       if __name__ = "__main__":
unittest.main()
