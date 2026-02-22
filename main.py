import requests
from bs4 import BeautifulSoup

url = "https://www.groza-motors.ru/catalog/mototsikly/"

# Получение данных с сайта
response = requests.get(url)

# Разбор полученных HTML-данных
soup = BeautifulSoup(response.text, "lxml")

# Получаем карточку товара
data = soup.find(class_="mt-auto px-1 leading-snug xl:space-y-1")

# Получаем название товара из класса html страницы
name = data.find(class_="non_decoration text-sm font-medium xl:text-xl js-notice-block__title").text.strip()
# С помощью метода text, выводим в консоль только текст.С помощью strip удаляем пробелы в начале и в конце сторки
print(name)
price = data.find(class_="font-semibold xl:text-2xl js-price-28913").text.strip()
print(price)
