import requests
from bs4 import BeautifulSoup
import openpyxl
import products

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

            print(f'Назва: {product_name}')
            print(f'Ціна: {product_price}')
            print('-' * 50)

            cena = ''.join(product_price[0:-3].split())
            print(cena)
            sheet.cell(row=row, column=1, value=product_name)
            sheet.cell(row=row, column=2, value=product_price)

        workbook.save('komputronik.xlsx')
    else:
        print(f'Помилка отримання сторінки. Статус-код: {response.status_code}')
# URL сторінки, яку потрібно спарсити

for i in range(1,10):
    url = f'https://www.komputronik.pl/search-filter/1099/geforce-rtx-3060?a%5B507%5D%5B%5D=130691&filter=1&showBuyActiveOnly=0&p={i}'
    open_surl(url)
    print('*' * 70)