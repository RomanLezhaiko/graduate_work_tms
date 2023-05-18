import time
import json

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

button_catalog = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/header/div/div[3]/div/button')
button_catalog.click()
time.sleep(2)

catalog_categories = driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/header/div[1]/div[5]/div/div[1]/div[1]')
soup = BeautifulSoup(catalog_categories.get_attribute('innerHTML'), "html.parser")
all_category_in_catalog = soup.findAll('a')


links = []
for category in all_category_in_catalog:
    if category.text == 'Сертификаты' or category.text == 'Товары для взрослых':
        continue
    
    links.append(f'https://www.21vek.by{category["href"]}')

category_list = []
i = 1

for link in links:
    driver.get(link)
    time.sleep(5)
    
    element = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/div[1]')
    soup = BeautifulSoup(element.get_attribute('innerHTML'), "html.parser")
    h1 = soup.find('h1', class_='content__header cr-category_header')
   
    tmp_dict = {
        'id': i,
        'name': h1.text,
        'parent_id': None
    }
    
    i += 1
    category_list.append(tmp_dict)
    
    category_sets = soup.findAll('div', class_='b-category-set')
    for category_set in category_sets:
        h2 = category_set.find('h2', class_='category-set__heading')
        h2_link = h2.find('a')
        
        tmp_dict_2 = {
            'id': i,
            'name': h2_link.text,
            'parent_id': tmp_dict['id']
        }
        
        i += 1
        category_list.append(tmp_dict_2)
        
        dts = category_set.findAll('dt')
        for dt in dts:
            dt_link = dt.find('a')
            
            tmp_dict_3 = {
                'id': i,
                'name': dt_link.text,
                'parent_id': tmp_dict_2['id'],
                'link': dt_link['href']
            }
            
            i += 1
            category_list.append(tmp_dict_3)
            


with open("/home/roman/dev/git_projects/graduate_work_tms/shop/parsing/parsing_category/category.json", "w") as outfile:
    json.dump(category_list, outfile, indent=4)  