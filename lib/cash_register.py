#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = 0
    self.last_transaction = 0
    self.items = []

  def add_item(self, item, price, quantity=1):
    self.item = item
    self.price = price
    self.last_transaction = price * quantity
    self.total += self.last_transaction

    self.last_item = []

    for i in range(quantity):
      self.last_item.append(item)

    self.items = self.items + self.last_item

  def apply_discount(self):
    if self.discount > 0:
      self.total = self.total * ((100 - self.discount)/100)
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print(f'There is no discount to apply.')

  def void_last_transaction(self):
    self.total -= self.last_transaction