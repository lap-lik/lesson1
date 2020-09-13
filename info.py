# Задание - Переменные
user_info = {
    'first_name' : 'Anton',
    'last_name' : 'Kokhno'
}
print(user_info['first_name'])
print('')#разделение
# Задание - Комплексные типы данных
list_1 = [3, 5, 7, 9, 10.5]
print(list_1)
print('') #разделение

list_1.append('Python')
print(len(list_1))
print('')#разделение

# next
print(list_1[0])
print('')#разделение

print(list_1[5])
print('')#разделение

print(list_1[1:4])
print('')#разделение

list_1.remove('Python')
print('проверка списка после удаления Python из него:')
print(list_1)
print('')#разделение
print('')#разделение
print('')#разделение

dict_1 = {"city": "Москва", "temperature": "20"}
print(dict_1['city'])
print(dict_1)
print('')
print('А теперь в сентябре')
dict_1['temperature'] = dict_1['temperature'] = '15'
print(dict_1)
print('')#разделение

print(dict_1.get('country'))
print('')#разделение

dict_1.get('country', 'Россия')
print(dict_1.get('country'))#НЕ РАБОТАЕТ!!!
print('')#разделение

dict_1['date'] = "27.05.2019"
print(dict_1)
print('')#разделение

print(len(dict_1))