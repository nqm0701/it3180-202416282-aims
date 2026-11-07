import unittest
from aims.cart import Cart
from aims.dvd import DigitalVideoDisc

class TestCartLimit(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        # Thêm 20 đĩa đầu tiên phải thành công (True)
        for i in range(20):
            dvd = DigitalVideoDisc(f"Title {i}", "Category", 10.0)
            self.assertTrue(cart.add_dvd(dvd))
        
        # Thêm đĩa thứ 21 phải bị từ chối và trả về False
        dvd_extra = DigitalVideoDisc("Extra Title", "Category", 10.0)
        self.assertFalse(cart.add_dvd(dvd_extra))

    def test_discount_calculation(self):
        cart = Cart()
        dvd = DigitalVideoDisc("Test DVD", "Category", 100.0)
        dvd.cost = 100.0
        cart.add_dvd(dvd)
        # Kiểm tra giảm giá 20% -> phải còn 80.0
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
        
        # Kiểm tra phần trăm không hợp lệ phải ném ra ValueError
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_sort_by_title(self):
        # Thêm các đĩa vào giỏ và kiểm tra thứ tự tiêu đề sau khi gọi sort_by_title()
        pass

    def test_sort_by_cost(self):
        # Kiểm tra thứ tự giá sau khi gọi sort_by_cost()
        pass

if __name__ == '__main__':
    unittest.main()