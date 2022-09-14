from datetime import date
from exceptions import ExceptionPriceValidate
from good_list_mixin import GoodListMixin


class Good:
  '''Класс товара'''

  def _validate_price(self, price):
      if type(price) is int:
          return price
      raise ExceptionPriceValidate

  def __ne__(self, other):
      return True if self.name != other.name else False

  def __init__(self, name: str, price:int, count: int, date_production:date, shelf_day:int):
      self.name = name
      self.count = count
      self.price = self._validate_price(price)
      self.date_production = date_production
      self.shelf_day = shelf_day


class GoodList(GoodListMixin):
  '''Класс со списком товаров'''

  def __str__(self):
      return f"Это список с товарами с количеством товаров: {len(self.good_list)}"

  def _get_goods_for_basic(self):
      """Функция, которая вернет данные для фабричного метода создания базового списка."""
      return [
          Good(name="Молоко", price=50, count=4, date_production=date(day=25, month=5, year=2022), shelf_day=45),
          Good(name="Колбаса", price=50, count=4, date_production=date(day=25, month=5, year=2022), shelf_day=45),
          Good(name="Хлеб", price=50, count=4, date_production=date(day=25, month=5, year=2022), shelf_day=45),
          Good(name="Куриные яйца", price=50, count=4, date_production=date(day=25, month=5, year=2022), shelf_day=45),
          Good(name="Рыба", price=50, count=4, date_production=date(day=25, month=5, year=2022), shelf_day=45),
      ]

  def make_good_list_basic(self):
      """Метод, который формирует список из базового товара."""
      basic_goods = self._get_goods_for_basic()

      for good in basic_goods:
        self.add_good_in_list(good)

  def __eq__(self, other):
      is_eq = True

      if len(self.good_list) != len(other.good_list):
        is_eq = False

      return is_eq

  def __repr__(self):
      return f"{id(GoodList)} {self.__doc__}"

  def __init__(self):
      self.good_list = []

  def get_good_list(self):
      return self.good_list

  def add_good_in_list(self, good: Good): #тип может быть только Goog
      '''Добавляем товар в список'''
      self.good_list.append(good)


good_list = GoodList()
good_list.make_good_list_basic()
print(good_list)
print(good_list.get_mean_price(good_list.get_good_list()))

good_list_second = GoodList()

with open('file.txt', 'r', encoding='utf-8') as file:
  list_with_goods = file.readlines()

  for str_good in list_with_goods:
      list_good = str_good.split(':')

      try:
          name = list_good[0]
          price = int(list_good[1])
          count = int(list_good[2])
          date_production = list_good[3]
          shelf_day = list_good[4]
          good_list.add_good_in_list(Good(name, price, count, date_production, shelf_day))
      except IndexError:
          print("Ошибка файла!")
          continue

first_good = Good(name="Молоко", price=50, count=4, date_production=date(day=25, month=5, year=2022), shelf_day=45)
second_good = Good(name="Колбаса", price=50, count=4, date_production=date(day=25, month=5, year=2022), shelf_day=45)
print(first_good != second_good)
print("Средняя цена: ", GoodList.get_mean_price(list_of_goods))
print("Максимальная цена: ", GoodList.get_good_with_max_price(list_of_goods))
print("Максимальное количество: ", GoodList.get_good_with_max_count(list_of_goods))
print(good_list)


