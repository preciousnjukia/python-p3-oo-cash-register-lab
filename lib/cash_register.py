#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = [] 

    def add_item(self, item_name, item_price, quantity=1):
        total_item_price = item_price * quantity
        self.total += total_item_price
        
        for _ in range(quantity):
            self.items.append(item_name)


        self.items.extend([item_name] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.total * self.discount) / 100
            self.total -= discount_amount
            self.total = max(self.total, 0)
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.items.pop()
            self.total -= last_item_price

    def reset_total(self):
        self.total = 0
        self.items = [] 