
class GoodListMixin:
    @staticmethod
    def get_mean_price(list_of_goods):
        '''Получаем среднюю цену товаров'''

        sum_price = 0
        sum_count = 0

        for good in list_of_goods:
            sum_price += int(good.price)
            sum_count += int(good.count)

        # print(f'sum goods = {sum_price}')
        # print(f'sum count = {sum_count}')

        mean = sum_price / sum_count

        return mean

    @staticmethod
    def get_good_with_max_price(list_of_goods):
        '''Получаем товар с максимальной ценой'''
        name = ''
        max_price = 0

        for good in list_of_goods:
            if good.price > max_price:
                max_price = good.price
                name = good.name

        return name

    @staticmethod
    def get_good_with_max_count(list_with_goods):
        '''Получаем товар с максимальным количеством'''

        name = ''
        max_count = 0

        for good in list_with_goods:
            if good.count > max_count:
                max_count = good.count
                name = good.name

        return name

    @staticmethod
    def get_good_with_min_count(list_with_goods):
        '''Получаем товар с минимальным количеством'''
        name = ''
        min_count = 0

        for good in list_with_goods:
            if good.count < min_count:
                min_count = good.count
                name = good.name

        return name

    @staticmethod
    def get_good_with_min_price(list_of_goods):
        '''Получаем товар с минимальной ценой'''
        name = ''
        min_price = 10000

        for good in list_of_goods:
            if good.price < min_price:
                min_price = good.price
                name = good.name

        return name
