#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0.0
    self.items = []
    self.last_transaction_amount = 0.0

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.items.extend([title] * quantity)
    self.last_transaction_amount = price * quantity

  def apply_discount(self):
    if self.discount:
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        new_total = int(self.total)
        print(f"After the discount, the total comes to ${new_total}.")
        return self.total
    else:
        print("There is no discount to apply.")

  def void_last_transaction(self):
        self.total -= self.last_transaction_amount
    

'''
class ShoppingCart:
    def __init__(self, coupon=0):
        self.coupon = coupon

    def checkout(self):
        total = sum([item.price for item in self.shopping_cart()])
        total -= total * self.coupon / 100
        return total
'''