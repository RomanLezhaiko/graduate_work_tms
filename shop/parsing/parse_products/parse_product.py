import time
import json
from decimal import Decimal

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://21vek.by/")
time.sleep(5)


button_cookies = driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/div/button[2]')
button_cookies.click()
time.sleep(2)


products_by_category = []
with open('E:\\R\python_projects\\parsing_21_vek\\parse_products\\products_by_category.json','r') as f:
    products_by_category = json.load(f)

id = 1
products_data = []
for tmp_dict in products_by_category:
    products_dict = tmp_dict['products']
    
    for key, value in products_dict.items():
        driver.get(value)
        time.sleep(5)
        
        pageSource = driver.find_element(By.XPATH, "//*").get_attribute("outerHTML")
        tmp_soup = BeautifulSoup(pageSource, "html.parser")
        
        keywords_html = tmp_soup.find('meta', {"name":"keywords"})
        keywords = keywords_html["content"] if keywords_html else ''
        keywords = keywords.replace('  ', ', ')
        keywords = keywords.replace('  ', ' ')
        # print(keywords)
        
        product = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div[1]')
        soup = BeautifulSoup(product.get_attribute('innerHTML'), "html.parser")
        h1 = soup.find('h1')
        # print(h1.text)
        
        description_html = soup.find('div', class_='b-info cr-info-descr')
        description = description_html.text if description_html else ''
        # print(description.strip())
        
        attributes_dict = {}
        attributes_html = soup.find('div', class_='b-info cr-info-attrs')
        attributes_list_html = attributes_html.findAll('div', class_='b-attrs columns__nowrap')
        for attr_html in attributes_list_html:
            header_html = attr_html.find('div', class_='attr__header')
            if header_html.text != 'Дополнительные материалы':            
                # print(header_html.text)
                attr_dict = {}
                attr_list = attr_html.findAll('div', class_='attr_item')
                for attr_item in attr_list:
                    key_1 = attr_item.find('span', class_='attr__name').text.strip()
                    value_1 = attr_item.find('span', class_='attr__value').text.strip()
                    value_1 = value_1.replace('\xa0', ' ')
                    attr_dict[key_1] = value_1
                
                attributes_dict[header_html.text] = attr_dict
        
        
        # print(attributes_dict)
        
        price_html = soup.find('span', {'itemprop': 'price'})
        price = price_html['data-price'] if price_html else ''
        # print(price)
        
        
        image_div = soup.find('div', class_='fotorama__frame fotorama__frame_active')
        image_html = image_div.find('img')
        print(image_html['src'])
        
        style_list = image_html['style'].split(';')
        width = 100
        height = 100
        for style in style_list:
            style = style.strip()
            if style.startswith('width'):
                width_list = style.split(':')
                width = width_list[1].replace('px', '')
            
            if style.startswith('height'):
                height_list = style.split(':')
                height = height_list[1].replace('px', '')
        
        # print(int(width), int(height))
        
        product_dict = {
            'id': id,
            'product_link': value,
            'name': h1.text,
            'category': tmp_dict['id'],
            'keywords': keywords,
            'description': description,
            'attributes': attributes_dict,
            'price': price,
            'main_image_href': image_html['src'],
            'image_width': int(width),
            'image_height': int(height),
        }
        
        products_data.append(product_dict)
        
        with open("E:\\R\python_projects\\parsing_21_vek\\parse_products\\products_data.json", "w") as outfile:
            json.dump(products_data, outfile, indent=4)
        
        id += 1
        print('Next id:', id)