import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}


    @property
    def name_items (self):
        return self.__name_items
    
    @property
    def number_items (self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            print ('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif self.__item_name not in self.__item_price:
            raise NameError ('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1
    
    def delete_item_from_check (self, name):
        if name not in self.__name_items:
            raise NameError ('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1
    
    def check_amount (self, name):
        total = []
        for item in self.__name_items:
            if item in self.__item_price:
               total.append(self.__item_price[item])
        if len(total) > 10:
                sum_total = sum(total) * 0.9
        else: 
                sum_total = sum(total)
        return sum_total
    
    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []

        for item in self.__name_items:
            if item in self.__tax_rate and self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item] * 0.2)

        return total

    

    def ten_percent_tax_calculation (self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if item in self.__tax_rate and self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item] * 0.1)

        return total

    def total_tax (self):
        return sum(self.ten_percent_tax_calculation() + self.twenty_percent_tax_calculation()) 

    @staticmethod
    def get_telephone_number(self, telephone_number):
        
        try:
            int(telephone_number)
        except ValueError:
            raise ValueError ('Необходимо ввести цифры')
        if len(telephone_number) > 10:
            raise ValueError ('Необходимо ввести 10 цифр после "+7"')
        return f'+7{telephone_number}'
