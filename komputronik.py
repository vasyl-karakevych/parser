import requests
from bs4 import BeautifulSoup
import openpyxl
from product import Product

def open_surl(url):
    # Відправка запиту до сторінки і отримання її вмісту
    response = requests.get(url)

    # Перевірка статус-коду відповіді
    if response.status_code == 200:
        # Парсимо HTML-сторінку
        soup = BeautifulSoup(response.text, 'html.parser')

        # Знаходимо всі елементи з назвою товару і ціною
        product_names = soup.find_all('h2', class_='font-headline text-lg font-bold leading-6 line-clamp-3 md:text-xl md:leading-8')
        prices = soup.find_all('div', class_='text-3xl font-bold leading-8')

        workbook = openpyxl.Workbook()
        sheet = workbook.active

        # Виводимо дані на екран
        for row, (name, price) in enumerate(zip(product_names, prices), start=1):
            product_name = name.text.strip()
            product_price = price.text.strip()

            product_price = ''.join(product_price[0:-3].split())

            sheet.cell(row=row, column=1, value=product_name)
            sheet.cell(row=row, column=2, value=product_price)

         # Видаляємо якщо пише у назві OUTLET   
            if product_name[-7:-1] == "Outlet": 
                continue

            products = Product(product_name, product_price)
            list_products.append(products)

        workbook.save('komputronik.xlsx')
    else:
        print(f'Помилка отримання сторінки. Статус-код: {response.status_code}')
# URL сторінки, яку потрібно спарсити

def fiter_list(list_products):
    # Створюємо словник для відстеження унікальних імен
    unique_names = {}

    # Фільтруємо список, залишаючи тільки об'єкти з унікальними іменами
    filtered_products = []

    for product in list_products:
        if product.name not in unique_names:
            unique_names[product.name] = True
            filtered_products.append(product)
    list_products = filtered_products

    # Фільтрумемо ті які містять в назві outlet
    # for product in list_products:
    #     if product.name.find('oferta Outlet'):
    #         print('outlet')

    return list_products


list_products = []
for i in range(1,4):
    url = f'https://www.komputronik.pl/search-filter/1099/geforce-rtx-3060?a%5B507%5D%5B%5D=130691&filter=1&showBuyActiveOnly=0&p={i}'
    open_surl(url)
    print('*' * i)

list_products = fiter_list(list_products)

print(list_products)
print(f'count= {len(list_products)}')
