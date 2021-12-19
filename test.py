import requests


print('Создадим пользователя:')
response = requests.put(
    'http://localhost:5000/user/yulia',
    {'password': '1874'}
)
print(response.json())

print('Создадим еще одного пользователя ( пароль тот же):')
response = requests.put(
    'http://localhost:5000/user/masha',
    {'password': '1874'}
)
print(response.json())

print('Попробуем сделать пользователя с существующим ником:')
response = requests.put(
    'http://localhost:5000/user/yulia',
    {'password': '1874'}
)
print(response.json())

print('Получим данные пользователя:')
response = requests.get('http://localhost:5000/user/yulia ')
print(response.json())

print('Удалим пользователя:')
response = requests.delete('http://localhost:5000/user/yulia')
print(response.text)

print('Попытаемся получить информацию о несуществующем пользователе:')
response = requests.get('http://localhost:5000/user/yulia')
print(response.json())
