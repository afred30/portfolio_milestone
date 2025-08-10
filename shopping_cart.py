class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = float(item_price)
        self.item_quantity = int(item_quantity)

    def print_item_cost(self):
        # Helper to format dollars like examples (no .00 if whole dollars)
        def money(n):
            return f"${int(n)}" if n == int(n) else f"${n:.2f}"
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ {money(self.item_price)} = {money(total_cost)}")


if __name__ == "__main__":
    # Step 2: prompt for two items and create two objects
    print("Item 1\n")
    name1 = input("Enter the item name:\n")
    price1 = float(input("\nEnter the item price:\n"))
    qty1 = int(input("\nEnter the item quantity:\n"))

    print("\nItem 2\n")
    name2 = input("Enter the item name:\n")
    price2 = float(input("\nEnter the item price:\n"))
    qty2 = int(input("\nEnter the item quantity:\n"))

    item1 = ItemToPurchase(name1, price1, qty1)
    item2 = ItemToPurchase(name2, price2, qty2)

    # Step 3: print total cost details
    def money(n):
        return f"${int(n)}" if n == int(n) else f"${n:.2f}"

    print("\nTOTAL COST\n")
    item1.print_item_cost()
    item2.print_item_cost()
    grand_total = item1.item_price * item1.item_quantity + item2.item_price * item2.item_quantity
    print(f"\nTotal: {money(grand_total)}")

