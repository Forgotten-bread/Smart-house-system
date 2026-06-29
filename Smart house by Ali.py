def request_list (request):
    i = (request.split())
    if i[0] == f'{name},': return 'Выполняю'
    else: return 'Нахожусь в режиме ожидания'
name = input('Введите имя вашего умного дома: ')
requesto = input('Ваша фраза: ')
print(request_list(requesto))
