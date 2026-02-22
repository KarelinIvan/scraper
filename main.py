import requests
from bs4 import BeautifulSoup

url = "https://www.groza-motors.ru/catalog/mototsikly/"

# Получение данных с сайта
response = requests.get(url)

# Разбор полученных HTML-данных
soup = BeautifulSoup(response.text, "lxml")

# Получаем карточку товара
data = soup.find_all(class_="js-load-content1")

# Создаем цикл, чтобы пройтись по всем карточкам товаров на странице
for i in data:
    # Получаем название товара из класса html страницы
    # С помощью метода text, выводим в консоль только текст.С помощью strip удаляем пробелы в начале и в конце сторки
    name = i.find(class_="non_decoration text-sm font-medium xl:text-xl js-notice-block__title").text.strip()

    # Получаем цену товара
    price = i.find(class_="card-product-card__prices").text.strip()
    # Выводим данные о статусе товара в магазине
    product_availability = i.find(class_="product-amount_title").text
    print(f"Наименование товара: {name} Цена: {price} Статус: {product_availability}")
