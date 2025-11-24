import sqlalchemy
import os
from pprint import pprint
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy.orm import sessionmaker
from Model import create_tables, Publisher, Book, Stock, Shop, Sale

SQLsystem = os.getenv('SQLsystem')
login = os.getenv('login')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
db_name = os.getenv('db_name')

DSN = f'{SQLsystem}://{login}:{password}@{host}:{port}/{db_name}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()


publisher1 = Publisher(name='АСТ')
publisher2 = Publisher(name='Вита Нова')
publisher3 = Publisher(name='Эксмо')
session.add_all([publisher1, publisher2, publisher3])


book1 = Book(title='Пучко Л. Г. "Биолокация для всех"', publisher=publisher1)
book2 = Book(title='Байба С. "Ведическая нумерология"', publisher=publisher1)
book3 = Book(title='Черняков Ю. "Тело как феномен"', publisher=publisher1)
book4 = Book(title='Кочергин Э "Ангелова кукла"', publisher=publisher2)
book5 = Book(title='Достоевский Ф. М. "Ранняя проза"', publisher=publisher2)
book6 = Book(title='Кэрролл Л. "Приключения Алисы в стране чудес"', publisher=publisher2)
book7 = Book(title='Арден Л. "Невеста ноября"', publisher=publisher3)
book8 = Book(title='Олкотт Л. М. "Маленькие женщины"', publisher=publisher3)
book9 = Book(title='Бредбери Р. "Вино из одуванчиков"', publisher=publisher3)

session.add_all([book1, book2, book3, book4, book5, book6, book7, book8, book9])

shop1 = Shop(name='Labirint')
shop2 = Shop(name='OZON')
shop3 = Shop(name='Amazon')

session.add_all([shop1, shop2, shop3])

stock1 = Stock(count=50, id_book=1, id_shop= 1)
stock2 = Stock(count=100, id_book=8, id_shop=1)
stock3 = Stock(count=120, id_book=2, id_shop=1)
stock4 = Stock(count=170, id_book=3, id_shop=2)
stock5 = Stock(count=10, id_book=5, id_shop=2)
stock6 = Stock(count=20, id_book=7, id_shop=2)
stock7 = Stock(count=70, id_book=9, id_shop=3)
stock8 = Stock(count=15, id_book=4, id_shop=3)
stock9 = Stock(count=19, id_book=6, id_shop=3)
stock10 = Stock(count=20, id_book=6, id_shop=1)
stock11 = Stock(count=55, id_book=1, id_shop=2)
stock12 = Stock(count=60, id_book=2, id_shop=3)

session.add_all([stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8, stock9, stock10, stock11, stock12])

sale1 = Sale(price=50.05, date_sale='2023-1-25', count=5, id_stock=1)
sale2 = Sale(price=60.00, date_sale='2023-1-25', count=7, id_stock=3)
sale3 = Sale(price=65.10, date_sale='2023-1-26', count=10, id_stock=5)
sale4 = Sale(price=70.00, date_sale='2023-1-26', count=34, id_stock=10)
sale5 = Sale(price=20.35, date_sale='2023-1-27', count=2, id_stock=7)
sale6 = Sale(price=30.00, date_sale='2023-1-27', count=23, id_stock=4)

session.add_all([sale1, sale2, sale3, sale4, sale5, sale6])

session.commit()

         #Выборки


publisher_id = input('Введите идентификатор издателя ')
for c in session.query(Shop.name).join(Stock.shop).join(Stock.book).\
        join(Book.publisher).filter(Publisher.id == publisher_id).all():
    pprint(c)

publisher_name = input('Введите название издателя ')
for c in session.query(Shop.name).join(Stock.shop).join(Stock.book).\
        join(Book.publisher).filter(Publisher.name == publisher_name).all():
    pprint(c)

publisher_id = input('Введите идентификатор издателя: ')
for c in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).\
                join(Stock.shop).join(Stock.book).join(Book.publisher).\
                join(Stock.sale).filter(Publisher.id == publisher_id):
            pprint(c)

publisher_name = input('Введите название издателя: ')
for c in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).\
                join(Stock.shop).join(Stock.book).join(Book.publisher).\
                join(Stock.sale).filter(Publisher.name == publisher_name):
            pprint(c)