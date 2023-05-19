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


products_data = []
with open('E:\\R\\python_projects\\parsing_21_vek\\parse_products_image\\products_data.json','r') as f:
    products_data = json.load(f)


images_list = []
for tmp_dict in products_data:
    driver.get(tmp_dict['product_link'])
    time.sleep(5)
    
    pageSource = driver.find_element(By.XPATH, "//*").get_attribute("outerHTML")
    soup = BeautifulSoup(pageSource, "html.parser")
    
    fotorama_frames = soup.findAll('div', class_='fotorama__frame')
    
    for frame in fotorama_frames:
        image_dict = {}
        image_html = frame.find('img')
        
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
        
        image_dict = {
            'product_id': tmp_dict['id'],
            'image_href': image_html['src'],
            'width': int(width.strip()),
            'height': int(height.strip()),
        }
        
        images_list.append(image_dict)
        
        with open("E:\\R\\python_projects\\parsing_21_vek\\parse_products_image\\products_image_data.json", "w") as outfile:
            json.dump(images_list, outfile, indent=4)


driver.close()