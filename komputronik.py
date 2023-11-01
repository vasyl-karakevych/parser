import requests
from bs4 import BeautifulSoup
import openpyxl
from product import Product

def Open_url(url):
    # Відправка запиту до сторінки і отримання її вмісту
    response = requests.get(url)

    # Перевірка статус-коду відповіді
    if response.status_code == 200:
        # Парсимо HTML-сторінку
        soup = BeautifulSoup(response.text, 'html.parser')

        # Знаходимо всі елементи з назвою товару і ціною
        product_names = soup.find_all('h2', class_='font-headline text-lg font-bold leading-6 line-clamp-3 md:text-xl md:leading-8')
        prices = soup.find_all('div', class_='text-3xl font-bold leading-8')
        # font-semibold

        # Виводимо дані на екран
        for row, (name, price) in enumerate(zip(product_names, prices), start=1):
            product_name = name.text.strip()
            product_price = price.text.strip()

            product_price = ''.join(product_price[0:-3].split())

        # Видаляємо якщо пише у назві OUTLET   
            if product_name[-7:-1] == "Outlet": 
                continue

            products = Product(product_name, int(product_price))
            list_products.append(products)

        
    else:
        print(f'Помилка отримання сторінки. Статус-код: {response.status_code}')
# URL сторінки, яку потрібно спарсити

def Fiter_List(list_products):
    # Створюємо словник для відстеження унікальних імен
    unique_names = {}

    # Фільтруємо список, залишаючи тільки об'єкти з унікальними іменами
    filtered_products = []

    for product in list_products:
        if product.name not in unique_names:
            unique_names[product.name] = True
            filtered_products.append(product)
    list_products = filtered_products
    return list_products
def Write_Exel(list_product):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    
    for row, (product) in enumerate(list_products, start=1):
        sheet.cell(row=row, column=1, value=product.getName())
        sheet.cell(row=row, column=2, value=product.getPrice())
    
    workbook.save('komputronik.xlsx')
def Sort(list_products):
    for i in range(0, len(list_products)-1):
        for j in range(i, len(list_products)):
            if list_products[i].getPrice() >  list_products[j].getPrice():
                tmp_name = list_products[i].getName()
                tmp_price = list_products[i].getPrice()
                list_products[i].setName(list_products[j].getName())
                list_products[i].setPrice(list_products[j].getPrice())
                list_products[j].setName(tmp_name)
                list_products[j].setPrice(tmp_price)
                if i > 1:
                    i = i - 2
    return list_products

list_products = []
for i in range(1,4):
    url = f'https://www.komputronik.pl/search-filter/1099/geforce-rtx-3060?a%5B507%5D%5B%5D=130691&filter=1&showBuyActiveOnly=0&p={i}'
    Open_url(url)
    print('*' * i)

list_products = Fiter_List(list_products)
Write_Exel(list_products)

print(list_products)
Sort(list_products)
print(list_products)
# print(f'count= {len(list_products)}')
