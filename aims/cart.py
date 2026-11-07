MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD (lỗi)."""

    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
        else:
            print("--- CART ITEMS ---")
            for dvd in self.items:
                print(f"- {dvd.title} [{dvd.category}]: {dvd.cost} $")
            print(f"Total cost: {self.total_cost():.2f} $")

    def total_cost_with_discount(self, percent):
        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100")
        total = sum(item.cost for item in self.items)
        return total * (1 - percent / 100)

    def filter_by_category(self, category):
        return [dvd for dvd in self.items if dvd.category == category]

    def sort_by_title(self):
        """Sắp xếp các đĩa trong giỏ hàng theo tiêu đề (A-Z)."""
        self.items.sort(key=lambda dvd: dvd.title)

    def sort_by_cost(self):
        """Sắp xếp các đĩa trong giỏ hàng theo giá giảm dần."""
        self.items.sort(key=lambda dvd: dvd.cost, reverse=True)

    def clear(self):
        self.items.clear()
