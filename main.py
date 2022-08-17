class Good:
  '''Класс товара'''

  def __init__(self, name, count, price):
      self.name = name
      self.count = count
      self.price = price

class GoodList:
  '''Класс со списком товаров'''

  def __str__(self):
      return f"Это список с товарами с количеством товаров: {len(self.good_list)}"

  def __eq__(self, other):
      is_eq = True

      if len(self.good_list) != len(other.good_list):
        is_eq = False

      return is_eq

  def __init__(self):
      self.good_list = []

  def add_good_in_list(self, good: Good): #тип может быть только Goog
      '''Добавляем товар в список'''

      self.good_list.append(good)

  def get_mean_price(self):
      '''Получаем среднюю цену товаров'''

      sum_price = 0
      sum_count = 0

      for good in self.good_list:
          sum_price += int(good.price)
          sum_count += int(good.count)

      # print(f'sum goods = {sum_price}')
      # print(f'sum count = {sum_count}')

      mean = sum_price / sum_count

      return mean


  def get_good_with_max_price(self):
      '''Получаем товар с максимальной ценой'''

      name = ''
      max_price = 0

      for good in self.good_list:
          if good.price > max_price:
              max_price = good.price
              name = good.name

      return name

  def get_good_with_min_price(self):
      '''Получаем товар с минимальной ценой'''

      name = ''
      min_price = 10000

      for good in self.good_list:
          if good.price < min_price:
              min_price = good.price
              name = good.name

      return name

  def get_good_with_max_count(self):
      '''Получаем товар с максимальным количеством'''

      name = ''
      max_count = 0

      for good in list_with_goods:
          if good.count > max_count:
              max_count = good.count
              name = good.name

      return name

  def get_good_with_min_count(self):
      '''Получаем товар с максимальным количеством'''

      name = ''
      min_count = 0

      for good in list_with_goods:
          if good.count < min_count:
              min_count = good.count
              name = good.name

      return name


good_list = GoodList()
good_list_second = GoodList()

with open('file.txt', 'r') as file:
  list_with_goods = file.readlines()

  for str_good in list_with_goods:
      list_good = str_good.split(':')

      try:
          name = list_good[0]
          price = list_good[1]
          count = list_good[2]
      except IndexError:
          print("Ошибка файла!")
          continue

      good_list_second.add_good_in_list(Good(name, price, count))
      good_list.add_good_in_list(Good(name, price, count))
      good_list.get_mean_price()

info_str = str(good_list)
print(info_str)
print(good_list == good_list_second)