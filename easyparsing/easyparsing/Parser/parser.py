import pymysql
from easyparsing.easyparsing.db_config.config import *
import requests
from bs4 import BeautifulSoup
import json


def dict_loader(item, page_counter):
    tbl_column_name_dict['Link'] = 'https://www.wildberries.ru/catalog/' + str(item['nmId']) + '/detail.aspx' \
                                                                                               '?targetUrl=GP '
    tpl = tbl_column_name_dict['Date'], tbl_column_name_dict['Category'], tbl_column_name_dict['Under_Category'], \
           tbl_column_name_dict['Link'], item['nmId'], item['name'], item['price'], item['salePrice'],\
           item['feedbacks'], item['sale'], page_counter, item['brand']
    return tpl



def connect_db():
    try:
        con = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )

        cur = con.cursor()

    except Exception as ex:
        print('Connection refused...\n', ex)

    try:
        req = requests.get(wb, headers).text
        soup = BeautifulSoup(req)
        category = soup.find('ul', attrs={'class': 'menu-burger__main-list'}).find_all('a')
        for link in category:
            tbl_column_name_dict['Category'] = link.text
            request_to_category = requests.get(link.get('href'), headers).text
            soup_category = BeautifulSoup(request_to_category)
            category_menu = soup_category.find('div', attrs={'class': 'menu-catalog'})
            for link_under_cat in category_menu.find_all('a'):
                tbl_column_name_dict['Under_Category'] = link_under_cat.text
                req_under_cat = requests.get(catalog_data + link_under_cat.get('href').replace('/catalog/', '') + '?').text
                page_counter = 1
                json_pcl = json.loads(req_under_cat)
                qty_page = json_pcl['value']['data']['model']['pagerModel']['pagingInfo']['totalPages']
                while page_counter <= qty_page:
                    req_under_cat = requests.get(catalog_data + link_under_cat.get('href').replace('/catalog/', '') +
                                                 '?' + str(page_counter)).text
                    json_pcl = json.loads(req_under_cat)
                    position = 1
                    for item in json_pcl['value']['data']['model']['products']:
                        position = 1
                        cur.execute(sql_str, dict_loader(item, position))
                        position += 1
                    con.commit()
                    print('commit page: ', page_counter)
                    page_counter += 1


    except Exception as ex:
        print('faild: ', ex)

    con.close()
