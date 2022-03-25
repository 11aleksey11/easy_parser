import datetime

host = 'easypaom.beget.tech'
user = 'easypaom_shop'
password = 'mj3b4L2P'
db_name = 'easypaom_shop'


tbl_column_name_dict = {
    'Date': datetime.date.today(),
    'Category': '',
    'Under_Category': '',
    'Link': '',
    'Article': 0,
    'Produxt_name': '',
    'Price': 0,
    'Price_to_sales': 0,
    'Qty_feedback': 0,
    'Qty_sold': 0,
    'Page_number': 0,
    'Brand': ''

}

wb = 'https://www.wildberries.ru/'
catalog_data = 'https://www.wildberries.ru/catalogdata/'
headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 ' \
          'Safari/537.36 '
sql_str = 'insert into wb_table(Date, Category, Under_Category, Link, Article, Product_name, Price, ' \
          'Price_to_sales, Qty_feedback, Qty_sold, Page_number, Brand) values(%s, %s, %s, %s, %s, %s, %s, ' \
          '%s, %s, %s, %s, %s)'

