# Пример - Функции
price = 100
discount = 5
pruce_with_discount = price - price * discount / 100
print(pruce_with_discount)
print('')#разделение

def discounted(price, discount):
    price_with_discount = price - (price * discount / 100)
    print(price_with_discount)
price1 = 100
discount1 = 10
discounted(price1, discount1)
print('')#разделение
print('')#разделение

# Задание - Функции
def get_summ(one, two, delimiter='&'):
    summ = one + delimiter + two
    return summ
x = get_summ('Learn', 'python')
print(x)
print('')#разделение

# Задание - Функции next
def format_price(price):
    price = int(price)
    x_price = f'Цена: {price} руб.'
    return x_price

z = format_price(56.24)
print(z)