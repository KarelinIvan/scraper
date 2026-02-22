import requests
from bs4 import BeautifulSoup
from time import sleep

url = "https://www.groza-motors.ru/catalog/mototsikly/"

# Скрываем от сайта, что это парсер
headers={'User-agent': 'Mozilla /5.0 (Windows NT 8; Win64; x64) AppleWebKit /729.0 Safari'}

# Получение данных с сайта
response = requests.get(url, headers=headers)

# Разбор полученных HTML-данных
soup = BeautifulSoup(response.text, "lxml")

# Получаем карточку товара
data = soup.find_all(class_="js-load-content1")

# Создаем цикл, чтобы пройтись по всем карточкам товаров на странице
for i in data:
    # Делаем задержку в 3 секунд между запросами, чтобы не забанили
    sleep(3)
    # Получаем название товара из класса html страницы
    # С помощью метода text, выводим в консоль только текст.С помощью strip удаляем пробелы в начале и в конце сторки
    name = i.find(class_="non_decoration text-sm font-medium xl:text-xl js-notice-block__title").text.strip()

    # Получаем цену товара
    price = i.find(class_="card-product-card__prices").text.strip()

    # Выводим данные о статусе товара в магазине
    product_availability = i.find(class_="product-amount_title").text

    # Ссылка на товар
    url_product = "https://www.groza-motors.ru" + i.find(class_="non_decoration btn-main mt-auto w-full rounded-sm px-6 py-4 text-center font-semibold xl:hidden").get("href")

    # Принтуем данные в строку
    print(f"Наименование товара: {name} Цена: {price} Статус: {product_availability} Ссылка на товар: {url_product}")
